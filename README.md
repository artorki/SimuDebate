# 🧠 SimuDebate

### Multi-Agent Debate Simulator in a 3D Virtual Environment

> **SimuDebate** یک شبیه‌ساز مناظره‌ی چندعاملی است که چند Agent هوش مصنوعی با نقش‌ها، تخصص‌ها و مکاتب فکری متفاوت را در یک محیط سه‌بعدی قرار می‌دهد تا به‌جای پاسخ‌های مستقل، یک **بحث پویا، چنددیدگاهی و قابل تحلیل** شکل بگیرد.

کاربر به‌عنوان **Host** موضوع را تعیین می‌کند و Agentها در طول مناظره استدلال‌های یکدیگر را بررسی، تأیید، رد و در صورت نیاز اصلاح می‌کنند. هر Agent نیز وضعیت شناختی مستقل خود را حفظ می‌کند.

---

## ✨ امکانات

### 🏢 محیط سه‌بعدی تعاملی

محیط Virtual Office با **Three.js** شامل:

* سالن جلسات
* کتابخانه
* بایگانی
* اتاق سرور
* بخش برنامه‌نویسی
* دفتر مدیریت / روابط‌عمومی

کاراکترها دارای رفتارها و Animationهایی مانند **Walking، Sitting، Typing، Reading، Searching و Talking** هستند.

### 🧠 Cognitive State

هر Agent علاوه بر تاریخچه، یک State ساختاریافته دارد که شامل:
`beliefs`, `claims`, `supported_claims`, `challenged_claims`, `concessions`, `uncertainties`, `objectives` و `opponents` است.

### ⚡ Logical Interruption

سیستم می‌تواند پیش از هر نوبت بررسی کند که آیا **تناقض جدی، خطای فاحش یا حمله مستقیم** وجود دارد و در صورت نیاز یک وقفه‌ی کوتاه ایجاد کند.

### 🔀 Multi-Model

دو حالت:

* **Single:** یک مدل برای همه‌ی Agentها
* **Multi:** مدل و Provider مستقل برای هر Agent

پشتیبانی فعلی از **OpenAI، Claude، Gemini و مدل‌های Local سازگار با OpenAI API**.

### 📡 Telegram + Human-in-the-Loop

دریافت پیام‌های Telegram، ورود آن‌ها به جریان مناظره و ارسال پاسخ Agentها به Chat.

### 📊 تحلیل و خروجی

* **Synthesis:** جمع‌بندی نقاط توافق، اختلاف و مسیرهای پژوهشی
* **Mindmap:** تولید و رندر گراف ارتباطی با Mermaid.js
* **JSON Export:** خروجی کامل لاگ مناظره
* **Token & Cost Monitoring:** نمایش مصرف Token و هزینه‌ی تخمینی

### 💾 State Persistence

تنظیمات، تاریخچه، وضعیت Agentها، Mindmap و اطلاعات مناظره در `state.json` ذخیره و بازیابی می‌شوند.

### 🧩 Context Management

در بحث‌های طولانی، به‌جای ارسال کل Transcript، ادعاهای ابتدایی و نوبت‌های اخیر نگه داشته می‌شوند تا Context کنترل شود.

---

## 🏗️ معماری

```text
Frontend
HTML + JavaScript
├── Three.js
├── TailwindCSS
└── Mermaid.js

        ↓ HTTP / JSON

Backend
Python + Flask
├── LLM Routing
├── Telegram API
├── State Persistence
├── Token Tracking
└── Cost Estimation
```

---

## 🎯 کاربردها

**پژوهش و تحلیل** — بررسی یک مسئله از چند دیدگاه
**تولید محتوا** — ایده‌پردازی برای پادکست، ویدیو و سناریو
**ارزیابی LLMها** — مقایسه‌ی مدل‌ها در یک محیط مشترک
**آموزش** — شبیه‌سازی مناظره‌های علمی، فلسفی و تاریخی
**Human-in-the-Loop** — مشارکت مستقیم کاربر و Telegram

---

## ⚙️ اجرا

```bash
pip install flask flask-cors requests
python SimuDebate_server.py
```

سپس `simudebate.html` را در مرورگر اجرا کنید.

Backend به‌صورت پیش‌فرض روی:

```text
http://127.0.0.1:8765
```

در دسترس است.

---

## ⚠️ نکته

SimuDebate یک محیط آزمایشگاهی برای **Multi-Agent Reasoning** است؛ خروجی LLMها همچنان می‌تواند دارای خطا یا hallucination باشد. همچنین در نسخه‌ی فعلی، API Keyها در State ذخیره می‌شوند؛ بنابراین نسخه‌ی فعلی بیشتر برای استفاده‌ی **Local / Personal** مناسب است.

---

### فلسفه‌ی پروژه

> **SimuDebate تلاش می‌کند اختلاف دیدگاه بین Agentها را از یک متن ساده به یک تجربه‌ی زنده، بصری و قابل تحلیل تبدیل کند.**

**Think. Challenge. Concede. Debate.**
