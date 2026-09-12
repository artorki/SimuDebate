import json
import time
import requests
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # اجازه به مرورگر برای اتصال به این سرور (حل مشکل CORS)

PRICING_TABLE = {
    "gpt-4o": (0.005, 0.015),
    "gpt-4-turbo": (0.01, 0.03),
    "gpt-3.5": (0.0005, 0.0015),
    "claude-3-opus": (0.015, 0.075),
    "claude-3-sonnet": (0.003, 0.015),
    "claude-3-5-sonnet": (0.003, 0.015),
    "claude-3-haiku": (0.00025, 0.00125),
    "gemini-1.5-pro": (0.0035, 0.0105),
    "gemini-1.5-flash": (0.000075, 0.0003),
    "gemini-2.0-flash": (0.0001, 0.0004)
}

def calculate_cost(model_name, in_tokens, out_tokens):
    in_r, out_r = 0.0, 0.0
    model_lower = model_name.lower()
    
    if "local" in model_lower or "ollama" in model_lower:
        return 0.0
        
    for k, v in PRICING_TABLE.items():
        if k in model_lower:
            in_r, out_r = v
            break
            
    return (in_tokens / 1000.0) * in_r + (out_tokens / 1000.0) * out_r

@app.route('/api/llm', methods=['POST'])
def api_llm():
    data = request.json
    provider = data.get('provider')
    model = data.get('model')
    api_key_input = data.get('api_key')
    system_prompt = data.get('system_prompt')
    prompt = data.get('prompt')
    max_tokens = data.get('max_tokens', 2000)

    api_keys = [k.strip() for k in api_key_input.split(",")] if isinstance(api_key_input, str) else api_key_input
    if not api_keys or api_keys == [""]:
        return jsonify({"content": None, "tokens": 0, "cost": 0.0})

    for current_key in api_keys:
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if provider == "OpenAI" or provider == "Local (Ollama/LM Studio)":
                    url = "https://api.openai.com/v1/chat/completions" if provider == "OpenAI" else "http://localhost:11434/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {current_key}", "Content-Type": "application/json"}
                    payload = {
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt}
                        ],
                        "max_tokens": max_tokens,
                        "temperature": 0.7
                    }
                    response = requests.post(url, headers=headers, json=payload, timeout=60)
                    response.raise_for_status()
                    resp_data = response.json()
                    content = resp_data['choices'][0]['message']['content']
                    in_tok = resp_data.get('usage', {}).get('prompt_tokens', int(len(prompt.split()) * 1.3))
                    out_tok = resp_data.get('usage', {}).get('completion_tokens', int(len(content.split()) * 1.3))
                    cost = calculate_cost(model, in_tok, out_tok)
                    return jsonify({"content": content, "tokens": in_tok + out_tok, "cost": cost})

                elif provider == "Anthropic (Claude)":
                    url = "https://api.anthropic.com/v1/messages"
                    headers = {
                        "x-api-key": current_key,
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json"
                    }
                    payload = {
                        "model": model,
                        "system": system_prompt,
                        "messages": [{"role": "user", "content": prompt}],
                        "max_tokens": max_tokens,
                        "temperature": 0.7
                    }
                    response = requests.post(url, headers=headers, json=payload, timeout=60)
                    response.raise_for_status()
                    resp_data = response.json()
                    content = resp_data['content'][0]['text']
                    in_tok = resp_data.get('usage', {}).get('input_tokens', int(len(prompt.split()) * 1.3))
                    out_tok = resp_data.get('usage', {}).get('output_tokens', int(len(content.split()) * 1.3))
                    cost = calculate_cost(model, in_tok, out_tok)
                    return jsonify({"content": content, "tokens": in_tok + out_tok, "cost": cost})

                elif provider == "Google (Gemini)":
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
                    headers = {"Content-Type": "application/json", "x-goog-api-key": current_key}
                    payload = {
                        "systemInstruction": {"parts": [{"text": system_prompt}]},
                        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                        "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0.7}
                    }
                    response = requests.post(url, headers=headers, json=payload, timeout=60)
                    response.raise_for_status()
                    resp_data = response.json()
                    content = resp_data['candidates'][0]['content']['parts'][0]['text']
                    in_tok = resp_data.get('usageMetadata', {}).get('promptTokenCount', int(len(prompt.split()) * 1.3))
                    out_tok = resp_data.get('usageMetadata', {}).get('candidatesTokenCount', int(len(content.split()) * 1.3))
                    cost = calculate_cost(model, in_tok, out_tok)
                    return jsonify({"content": content, "tokens": in_tok + out_tok, "cost": cost})

            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code if e.response else None
                if status_code == 429 and attempt < max_retries - 1:
                    time.sleep(5) 
                    continue
                elif status_code in [401, 403, 400]:
                    break 
                elif status_code in [500, 502, 503, 504] and attempt < max_retries - 1:
                    time.sleep(3)
                    continue
                break
            except Exception as e:
                print(f"API Request Exception: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                    continue
                break

    return jsonify({"content": None, "tokens": 0, "cost": 0.0})

@app.route('/api/telegram/send', methods=['POST'])
def api_tg_send():
    data = request.json
    token = data.get('token')
    chat_id = data.get('chat_id')
    text = data.get('text')
    
    if not token or not chat_id:
        return jsonify({"status": "error"})
        
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, json=payload, timeout=5)
        return jsonify({"status": "ok"})
    except Exception as e:
        print(f"Telegram Send Error: {e}")
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/telegram/updates', methods=['GET'])
def api_tg_updates():
    token = request.args.get('token')
    chat_id = request.args.get('chat_id')
    offset = request.args.get('offset', type=int, default=0)
    
    if not token or not chat_id: 
        return jsonify({"updates": [], "offset": offset})
        
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    params = {"timeout": 2}
    if offset:
        params["offset"] = offset
        
    updates = []
    try:
        resp = requests.get(url, params=params, timeout=5).json()
        if resp.get("ok") and resp["result"]:
            for req in resp["result"]:
                new_offset = req["update_id"] + 1
                offset = max(offset if offset else 0, new_offset)
                msg = req.get("message", {})
                if str(msg.get("chat", {}).get("id")) == str(chat_id) and "text" in msg:
                    user_name = msg.get("from", {}).get("first_name", "User")
                    updates.append({"user": user_name, "text": msg["text"]})
    except Exception as e:
        print(f"Telegram Fetch Error: {e}")
        
    return jsonify({"updates": updates, "offset": offset})

@app.route('/api/state', methods=['GET', 'POST'])
def api_state():
    state_file = 'state.json'
    if request.method == 'POST':
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(request.json, f, ensure_ascii=False, indent=2)
        return jsonify({"status": "saved"})
    else:
        if os.path.exists(state_file):
            try:
                with open(state_file, 'r', encoding='utf-8') as f:
                    return jsonify(json.load(f))
            except Exception as e:
                print(f"State load error: {e}")
        return jsonify({})

if __name__ == '__main__':
    print("SimuDebate Local Server Running on http://127.0.0.1:8765")
    app.run(port=8765, debug=True)