# 🧠 SimuDebate

### Multi-Agent Debate Simulator in a 3D Virtual Environment

> یک شبیه‌ساز مناظره‌ی چندعاملی که LLMها را از یک گفت‌وگوی ساده خارج می‌کند و به یک میزگرد زنده، چنددیدگاهی و تعاملی تبدیل می‌کند.

---

## 🌌 ایده‌ی اصلی

**SimuDebate** یک شبیه‌ساز مناظره‌ی Multi-Agent است که به‌جای نمایش چند پاسخ جداگانه از چند مدل زبانی، چند **Agent با هویت، نقش، مکتب فکری و وضعیت شناختی مستقل** را در یک محیط مجازی سه‌بعدی قرار می‌دهد.

کاربر به‌عنوان **Host** یک موضوع چالش‌برانگیز را مطرح می‌کند و سپس چند مهمان هوش مصنوعی وارد بحث می‌شوند.

هر مهمان می‌تواند مثلاً:

* دانشمند، فیلسوف، پژوهشگر، تحلیلگر یا هر نقش تخصصی دیگری باشد.
* به یک مکتب یا دیدگاه فکری مشخص تعلق داشته باشد.
* موضع مستقل خود را حفظ کند.
* ادعاهای دیگران را تأیید یا رد کند.
* در طول بحث از مواضع قبلی خود عقب‌نشینی کند.
* نقاط ابهام و عدم‌قطعیت خود را ثبت کند.
* برای ادامه‌ی بحث هدف داشته باشد.
* و در واکنش به استدلال‌های دیگران، وارد تعامل مستقیم شود.

در نتیجه، خروجی SimuDebate صرفاً یک Transcript نیست؛ بلکه یک **فرآیند استدلالی چندمرحله‌ای با حافظه و وضعیت داخلی** است.

---

# ✨ Why SimuDebate?

چت‌بات‌های معمولی عمدتاً یک سؤال را می‌گیرند و یک پاسخ تولید می‌کنند.

SimuDebate سؤال متفاوتی می‌پرسد:

> **اگر چند ذهن مصنوعی با پیش‌فرض‌های متفاوت، نقش‌های تخصصی متفاوت و حافظه‌ی مستقل را در یک اتاق قرار دهیم، چه اتفاقی می‌افتد؟**

اینجا مدل‌ها فقط «پاسخ‌دهنده» نیستند؛ بلکه تبدیل می‌شوند به **شرکت‌کنندگان یک مناظره‌ی پویا**.

---

# 🚀 Key Features

## 1. 🏢 محیط مجازی سه‌بعدی

کل تجربه در یک **Virtual Office سه‌بعدی** ساخته شده با Three.js اتفاق می‌افتد.

محیط شامل فضاهای مختلف است:

* 💻 دپارتمان برنامه‌نویسی
* 🤝 سالن جلسات
* 📢 دفتر مدیریت / روابط‌عمومی
* 📚 کتابخانه و فضای استراحت
* 🗄️ بخش بایگانی
* ⚙️ اتاق سرور و شبکه

محیط صرفاً تزئینی نیست و به‌صورت Interactive طراحی شده است؛ کاربر می‌تواند بین بخش‌های مختلف حرکت کند و هر فضا عملکرد مخصوص خود را دارد.

---

## 2. 🤖 شخصیت‌ها و رفتارهای سه‌بعدی

Agentها در محیط به‌صورت Characterهای سه‌بعدی نمایش داده می‌شوند.

سیستم Character Animation شامل وضعیت‌هایی مانند:

* Walking
* Sitting
* Typing
* Reading
* Searching
* Talking
* Idle

است.

کاراکترها می‌توانند بین اتاق‌ها جابه‌جا شوند و متناسب با محل قرارگیری یا وضعیت خود، Animation متفاوت داشته باشند.

برای مثال:

> یک Agent ممکن است از کتابخانه خارج شود، وارد سالن جلسات شود، روی صندلی خود بنشیند و سپس وارد چرخه‌ی مناظره شود.

---

# 3. 🧠 Cognitive State — حافظه‌ی ساختاریافته‌ی Agent

یکی از اجزای اصلی معماری SimuDebate، نگهداری **وضعیت شناختی مستقل برای هر Agent** است.

به‌جای اینکه Agent در هر نوبت فقط Transcript کامل را دریافت کند، وضعیت داخلی ساختاریافته‌ای دارد که در طول مناظره به‌روزرسانی می‌شود.

ساختار فعلی شامل مواردی مانند:

```json
{
  "beliefs": [],
  "claims": [],
  "supported_claims": [],
  "challenged_claims": [],
  "concessions": [],
  "uncertainties": [],
  "objectives": [],
  "opponents": {}
}
```

### این یعنی Agent می‌تواند:

**Beliefs**

> باورهای پایه و پیش‌فرض‌های فکری خود را حفظ کند.

**Claims**

> ادعاهای جدیدی که در طول بحث مطرح کرده ثبت شوند.

**Supported Claims**

> ادعاهای سایر Agentها که آن‌ها را معتبر می‌داند نگهداری شوند.

**Challenged Claims**

> استدلال‌ها یا ادعاهایی که با آن‌ها مخالف است ذخیره شوند.

**Concessions**

> مواردی که Agent در طول بحث از آن‌ها عقب‌نشینی کرده یا موضع خود را اصلاح کرده ثبت شوند.

**Uncertainties**

> نقاطی که Agent در آن‌ها اطمینان کافی ندارد مشخص شوند.

**Objectives**

> اهداف Agent برای ادامه‌ی مناظره مشخص باشند.

**Opponents**

> وضعیت موضع Agent نسبت به سایر شرکت‌کنندگان نگهداری شود.

این معماری باعث می‌شود Agent صرفاً مجموعه‌ای از پاسخ‌های مستقل نباشد، بلکه یک **stateful participant** در جریان بحث باشد.

---

# 4. ⚡ Logical Interruption

مناظره در SimuDebate صرفاً یک چرخه‌ی خشک و نوبتی نیست.

پیش از تولید هر پاسخ اصلی، سیستم می‌تواند یک Agent دیگر را به‌عنوان **Interrupter** انتخاب کند و از آن بخواهد بررسی کند آیا شرایط یک وقفه وجود دارد یا نه.

معیارهای فعلی شامل مواردی مانند:

* تناقض شدید
* خطای فاحش
* حمله‌ی مستقیم

هستند.

اگر شرایط برقرار باشد، Agent می‌تواند یک **وقفه‌ی کوتاه و محدود** ایجاد کند.

ساختار خروجی interruption به‌صورت مجزا پردازش می‌شود:

```json
{
  "interrupt": true,
  "reason": "دلیل وقفه",
  "text": "جمله کوتاه وقفه"
}
```

هدف این مکانیزم، شبیه‌سازی بخشی از پویایی یک مناظره‌ی واقعی است؛ جایی که یک استدلال ممکن است آن‌قدر مهم یا مسئله‌دار باشد که شرکت‌کننده‌ی دیگر نتواند منتظر نوبت بعدی بماند.

> توجه: interruption در پیاده‌سازی فعلی به‌صورت یک رخداد مجزا در چرخه‌ی مناظره شبیه‌سازی می‌شود و به معنای قطع واقعی یک stream در میانه‌ی generation نیست.

---

# 5. 🔀 Multi-Model Routing

SimuDebate از دو حالت اصلی برای اتصال به مدل‌ها پشتیبانی می‌کند:

### Single Mode

یک Provider / Model مرکزی برای تمام مهمان‌ها استفاده می‌شود.

مناسب برای:

* تست سریع
* کاهش پیچیدگی تنظیمات
* استفاده اقتصادی‌تر
* مقایسه‌ی رفتار Agentها با یک مدل یکسان

---

### Multi Mode

هر مهمان می‌تواند تنظیمات مدل مستقلی داشته باشد.

برای هر Agent می‌توان Provider، Model و API Key جداگانه تعریف کرد.

Providerهای فعلی رابط کاربری شامل:

* OpenAI
* Anthropic / Claude
* Google / Gemini
* Local

هستند.

همچنین معماری Local از endpoint سازگار با API سبک OpenAI استفاده می‌کند که امکان استفاده از مدل‌های Local مانند Ollama را فراهم می‌کند.

### نتیجه

می‌توان یک مناظره را به یک محیط آزمایشگاهی برای مقایسه‌ی مدل‌ها تبدیل کرد:

```text
Agent A → OpenAI
Agent B → Claude
Agent C → Gemini
Agent D → Local Model
```

و سپس مشاهده کرد که مدل‌ها در یک مسئله‌ی مشترک چگونه رفتار می‌کنند.

---

# 6. 🧑‍💼 Host Interaction

کاربر در SimuDebate فقط تماشاگر نیست.

Host می‌تواند در طول مناظره مستقیماً وارد گفتگو شود و پیام خود را به‌عنوان یک participant انسانی به تاریخچه اضافه کند.

این قابلیت برای سناریوهایی مثل:

* مطرح کردن سؤال جدید
* اصلاح صورت مسئله
* درخواست توضیح
* به چالش کشیدن یک Agent
* تغییر جهت بحث

در نظر گرفته شده است.

---

# 7. 📡 Telegram Integration

SimuDebate می‌تواند به Telegram متصل شود تا مناظره از یک محیط محلی خارج شود و به یک کانال ارتباطی زنده تبدیل گردد.

### قابلیت‌های Telegram

* ارسال پیام‌های مناظره به Chat
* دریافت پیام‌های کاربران
* ورود پیام‌های دریافتی به Context مناظره
* ارسال پاسخ Agentها به Telegram
* نگهداری offset برای دریافت پیوسته‌ی Updateها

بنابراین Telegram می‌تواند به‌عنوان یک **Human-in-the-Loop Interface** عمل کند.

یک سناریوی نمونه:

```text
Telegram User
      ↓
Telegram Bot
      ↓
SimuDebate
      ↓
Agent Context
      ↓
Agent Response
      ↓
Telegram
```

---

# 8. 🧩 Synthesis — جمع‌بندی نهایی

پس از پایان مناظره، کاربر می‌تواند یک Agent تحلیلی را برای تولید **Synthesis** فراخوانی کند.

این مرحله با هدف استخراج:

1. نقاط توافق
2. نقاط اختلاف
3. مسیرها و نیازهای آینده‌ی پژوهش

انجام می‌شود.

هدف Synthesis این نیست که حتماً بین طرفین توافق مصنوعی ایجاد کند؛ بلکه قرار است ساختار واقعی اختلاف دیدگاه‌ها را روشن‌تر کند.

---

# 9. 🕸️ Mindmap / Argument Graph

پس از مناظره، SimuDebate می‌تواند Transcript را به یک **گراف ارتباطی** تبدیل کند.

مدل، ساختار Mermaid تولید می‌کند و سپس آن در UI با Mermaid.js رندر می‌شود.

این قابلیت برای دیدن مواردی مثل:

* ارتباط بین ادعاها
* مسیرهای استدلالی
* نقاط اختلاف
* روابط بین مواضع

مفید است.

نمونه‌ی ساده:

```text
Claim A
 ├── supports → Claim B
 ├── challenges → Claim C
 └── conflicts → Claim D
```

Mindmap در UI قابل تولید و مشاهده است و کد تولیدشده نیز در State پروژه نگهداری می‌شود.

---

# 10. 📥 Export Debate Log

هر مناظره را می‌توان به‌صورت فایل JSON ذخیره کرد.

ساختار Export شامل اطلاعاتی مانند:

* Topic
* Date
* Guests
* Role
* School
* Transcript

است.

این فایل می‌تواند برای:

* آرشیو
* تحلیل بعدی
* پردازش با ابزارهای دیگر
* ساخت دیتاست
* تولید محتوای چندصدایی
* استفاده در Workflowهای خارج از SimuDebate

به‌کار رود.

---

# 11. 💰 Token & Cost Monitoring

سیستم مصرف Token را در طول مناظره دنبال می‌کند و هزینه‌ی تخمینی را نمایش می‌دهد.

در UI دو مقدار اصلی قابل مشاهده است:

```text
Consumed Tokens
Estimated Cost
```

Backend نیز اطلاعات usage دریافت‌شده از Providerها را پردازش کرده و هزینه را بر اساس جدول قیمت داخلی محاسبه می‌کند.

برای مدل‌های Local نیز امکان درنظرگرفتن هزینه‌ی API وجود ندارد و منطق داخلی برای آن‌ها مسیر هزینه‌ی صفر در نظر گرفته است.

> مقدار هزینه نمایش‌داده‌شده یک **برآورد داخلی** بر اساس جدول Pricing موجود در کد است و نباید به‌عنوان صورتحساب رسمی Provider تلقی شود.

---

# 12. 🧠 Context Management

در مناظره‌های طولانی، ارسال کل Transcript به مدل در هر نوبت هم هزینه را افزایش می‌دهد و هم Context را سنگین می‌کند.

SimuDebate در تاریخچه‌های طولانی از یک روش ساده‌ی Context Reduction استفاده می‌کند.

هنگامی که تعداد پیام‌ها زیاد شود:

* چند ادعای ابتدایی حفظ می‌شوند.
* بخش میانی تاریخچه حذف می‌شود.
* نوبت‌های اخیر حفظ می‌شوند.

به این ترتیب مدل همچنان به:

```text
Initial Claims
        +
Recent Turns
        +
Current State
```

دسترسی دارد، بدون اینکه کل تاریخچه‌ی Raw همیشه دوباره ارسال شود.

---

# 13. 💾 Persistent State

وضعیت برنامه از طریق Backend ذخیره و بازیابی می‌شود.

State شامل اطلاعاتی مانند:

* تنظیمات پروژه
* تاریخچه‌ی گفتگو
* Turn Index
* وضعیت اجرای مناظره
* Guest States
* تنظیمات Telegram
* تنظیمات Provider / Model
* Mindmap
* Token Usage
* Estimated Cost

است.

Backend این اطلاعات را در فایل:

```text
state.json
```

ذخیره می‌کند.

بنابراین با اجرای مجدد برنامه می‌توان State قبلی را بازیابی کرد.

---

# 14. 🛡️ Agent Behavior Rules

Agentها با System Promptهایی هدایت می‌شوند تا پاسخ‌ها بیشتر در قالب یک **شخصیت تخصصی و مشارکت‌کننده‌ی مناظره** قرار بگیرند.

قواعد پایه‌ی فعلی شامل مواردی مانند:

### 🎓 Expert Behavior

Agent باید در نقش تخصصی تعریف‌شده‌ی خود باقی بماند.

### 📚 Evidence-Oriented Reasoning

Agent به ارجاع معتبر و پرهیز از ادعاهای ساختگی هدایت می‌شود.

### 🚫 No AI Clichés

از عبارات کلیشه‌ای و غیرضروری مانند معرفی خود به‌عنوان «مدل زبانی» جلوگیری می‌شود.

### 🎯 Goal-Oriented Discussion

Agent دارای objective مشخص برای ادامه‌ی بحث است.

### 👂 Active Engagement

Agent باید به محتوای مناظره و استدلال‌های قبلی واکنش نشان دهد، نه اینکه صرفاً یک متن عمومی تولید کند.

> این‌ها سیاست‌های رفتاری تعریف‌شده در Prompt هستند و به‌تنهایی تضمین ریاضی برای حذف hallucination یا خطای factual محسوب نمی‌شوند.

---

# 🏗️ Architecture

SimuDebate از دو بخش اصلی و نسبتاً مستقل تشکیل شده است.

```text
┌───────────────────────────────────────┐
│           Frontend / UI              │
│                                       │
│  HTML + TailwindCSS + Three.js       │
│  Mermaid.js + Browser Runtime        │
└──────────────────┬────────────────────┘
                   │ HTTP / JSON
                   ▼
┌───────────────────────────────────────┐
│          Backend / Engine             │
│                                       │
│  Python + Flask + Requests            │
│                                       │
│  ├── LLM Routing                      │
│  ├── Provider Adapters                │
│  ├── Telegram API                     │
│  ├── State Persistence                │
│  ├── Token Tracking                   │
│  └── Cost Estimation                  │
└───────────────────────────────────────┘
```

---

# 🧱 Technology Stack

### Frontend

* HTML5
* JavaScript
* Three.js
* OrbitControls
* TailwindCSS
* Mermaid.js
* Vazirmatn

### Backend

* Python
* Flask
* Flask-CORS
* Requests

### External Services

* OpenAI
* Anthropic
* Google Gemini
* Local LLM Endpoint
* Telegram Bot API

---

# 📂 Project Structure

ساختار منطقی پروژه:

```text
SimuDebate/
│
├── simudebate.html
├── SimuDebate_server.py
│
└── state.json
```

> `state.json` در زمان اجرا ایجاد/به‌روزرسانی می‌شود.

---

# ⚙️ Requirements

برای Backend به Python و پکیج‌های زیر نیاز دارید:

```bash
pip install flask flask-cors requests
```

Frontend از کتابخانه‌هایی مانند Three.js، Mermaid.js و TailwindCSS از طریق CDN استفاده می‌کند؛ بنابراین در حالت فعلی برای بارگذاری آن‌ها به دسترسی شبکه نیاز دارید.

---

# ▶️ Running SimuDebate

## 1. اجرای Backend

```bash
python SimuDebate_server.py
```

در صورت اجرای موفق، Backend روی:

```text
http://127.0.0.1:8765
```

در دسترس خواهد بود.

APIهای اصلی:

```text
POST /api/llm
POST /api/telegram/send
GET  /api/telegram/updates
GET  /api/state
POST /api/state
```

---

## 2. اجرای Frontend

فایل:

```text
simudebate.html
```

را در مرورگر باز کنید.

Frontend به‌صورت پیش‌فرض به Backend زیر متصل می‌شود:

```javascript
http://127.0.0.1:8765/api
```

بنابراین Backend باید در زمان استفاده از برنامه در حال اجرا باشد.

---

# 🎛️ Configuration

از داخل Interface می‌توانید تنظیم کنید:

### Debate

* Topic
* Maximum Turns
* Start / Stop
* Synthesis

### Guests

* تعداد مهمان‌ها
* نام
* Role
* School

تعداد مهمان‌ها در UI بین **۲ تا ۵** قابل تنظیم است.

### LLM

* Single / Multi Mode
* Provider
* Model
* API Key

### Telegram

* Enable / Disable
* Bot Token
* Chat ID

---

# 🧪 Example Scenario

موضوع:

> **آیا آگاهی صرفاً محصول فعالیت مغز است؟**

دو مهمان:

```text
Guest 1
Role: Neuroscientist
School: Materialism

Guest 2
Role: Philosopher
School: Idealism
```

سپس:

```text
Host
  ↓
Set Topic
  ↓
Agent 1
  ↓
Interruption Check
  ↓
Agent 2
  ↓
Interruption Check
  ↓
Agent 1
  ↓
...
  ↓
Synthesis
  ↓
Mindmap
  ↓
JSON Export
```

در طول این فرآیند، وضعیت شناختی هر Agent نیز به‌روزرسانی می‌شود.

---

# 🔬 Use Cases

## پژوهش و تحلیل

برای بررسی یک مسئله از چند زاویه‌ی فکری، علمی یا تخصصی.

## نویسندگی

برای آزمایش فرضیه‌ها، پیدا کردن نقاط ضعف یک ایده و تولید دیدگاه‌های متضاد پیش از نگارش مقاله، کتاب یا سناریو.

## تولید محتوا

برای ساخت بحث‌های چندصدایی، سناریوهای پادکست، ویدیوهای تحلیلی و محتوای تعاملی.

## ارزیابی LLMها

برای مقایسه‌ی مدل‌های مختلف در یک مسئله‌ی واحد و مشاهده‌ی تفاوت رفتار آن‌ها در یک محیط مشترک.

## آموزش

برای شبیه‌سازی مناظره‌های:

* علمی
* فلسفی
* تاریخی
* تحلیلی

و نمایش بصری تفاوت دیدگاه‌ها.

## Human-in-the-Loop

برای وارد کردن انسان به چرخه‌ی استدلال از طریق Host یا Telegram.

---

# ⚠️ Important Notes & Limitations

SimuDebate یک محیط آزمایشگاهی برای Multi-Agent Reasoning است؛ بنابراین خروجی مدل‌ها همچنان ممکن است اشتباه، ناقص یا غیرقابل‌اعتماد باشد.

### امنیت API Keys

در نسخه‌ی فعلی، Credentialها در State برنامه قرار می‌گیرند و State روی فایل `state.json` ذخیره می‌شود.

بنابراین این نسخه برای یک محیط شخصی / Local مناسب‌تر است و برای Production باید مکانیزم امن‌تری برای Secret Management درنظر گرفته شود.

### Context Compression

مدیریت Context فعلی یک روش ساده‌ی retention-based است و یک سیستم خلاصه‌سازی معنایی کامل محسوب نمی‌شود.

### Interruption

وقفه‌ها به‌صورت تصمیم‌گیری و ثبت رخداد در چرخه‌ی مناظره پیاده‌سازی شده‌اند و streaming واقعی برای قطع generation در وسط پاسخ وجود ندارد.

### Cost Tracking

هزینه‌ها بر اساس Pricing Table داخلی پروژه تخمین زده می‌شوند و با تغییر قیمت Providerها باید این جدول نیز به‌روزرسانی شود.

---

# 🛣️ Future Roadmap

چشم‌انداز توسعه‌ی SimuDebate می‌تواند شامل موارد زیر باشد:

* Streaming واقعی پاسخ Agentها
* Interruption در سطح Token / Stream
* Semantic Memory و Vector Database
* RAG و اتصال به منابع علمی واقعی
* Citation Verification
* Agent-specific Tool Use
* Web Search / Research Agent
* Timeline و Replay کامل مناظره
* ارزیابی خودکار کیفیت استدلال
* Scoring و Ranking برای Agentها
* Argument Graph پیشرفته‌تر
* Voice Input / Voice Output
* آواتارها و Animationهای غنی‌تر
* Secret Management امن
* Docker Deployment
* Multi-user Session Management
* Benchmark Mode برای مقایسه‌ی سیستماتیک مدل‌ها

---

# 🤝 Philosophy

هدف SimuDebate این نیست که ثابت کند «کدام Agent همیشه درست می‌گوید».

هدف این است که:

> **فرآیند برخورد دیدگاه‌ها را قابل مشاهده، قابل تحلیل و قابل آزمایش کنیم.**

وقتی چند Agent با پیش‌فرض‌های متفاوت، اهداف متفاوت و حافظه‌ی مستقل در یک محیط مشترک قرار می‌گیرند، مسئله فقط تولید متن نیست.

مسئله تبدیل می‌شود به:

```text
Belief
  ↓
Claim
  ↓
Challenge
  ↓
Defense
  ↓
Concession
  ↓
New Objective
  ↓
Next Turn
```

و دقیقاً همین چرخه، هسته‌ی SimuDebate است.

---

# 📜 License

این بخش را متناسب با License انتخابی پروژه تکمیل کنید.

---

# ⭐ SimuDebate

### A visual, stateful and multi-agent environment for exploring disagreement, reasoning and AI perspectives.

```text
Think.
Challenge.
Concede.
Debate.
```
