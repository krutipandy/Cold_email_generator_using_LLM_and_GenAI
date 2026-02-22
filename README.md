<h1 align="center">📧 Cold Email Generator — AI-Powered B2B Outreach Tool</h1>

<p align="center">
  <img src="https://img.shields.io/badge/LLM-Llama%203.1-blueviolet?style=for-the-badge&logo=meta&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-LangChain-1C3C3C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Vector%20DB-ChromaDB-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Type-GenAI%20Application-green?style=for-the-badge" />
</p>

<p align="center">
  An end-to-end <strong>Generative AI application</strong> that scrapes job postings from any company's careers page and automatically generates highly personalized cold emails — tailored to match your portfolio and skills. Built with <strong>Llama 3.1</strong>, <strong>LangChain</strong>, <strong>ChromaDB</strong>, and <strong>Streamlit</strong>.
</p>

---

## 🎬 Inspiration & Credit

> This project was built following and extending the concepts from this excellent tutorial:
>
> 📺 **[Cold Email Generator — End-to-End LLM Project (YouTube)](https://youtu.be/CO4E_9V6li0)**
>
> Full credit to the original creator for the clear walkthrough. This repo implements, structures, and extends those ideas into a clean, deployable project.

---

## 💡 What Does It Do?

Imagine you're a software or AI services company trying to reach potential clients. Instead of writing cold emails manually for every job posting you find, this tool does it for you — **automatically and intelligently**.
```
1. You paste a company's careers/job page URL
2. The tool scrapes and extracts the job description
3. It matches required skills to your portfolio using semantic search
4. It generates a personalized cold email with relevant portfolio links
```

The result? A highly targeted cold email in seconds, ready to send.

---

## 🏗️ Architecture Overview
```
┌─────────────────────────────────────────┐
│         Streamlit Frontend              │
│    (Paste URL → Generate Email)         │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│           LangChain Chain               │
│         (chains.py)                     │
│  ┌─────────────┐   ┌─────────────────┐  │
│  │  Web Scraper│   │  Llama 3.1 LLM  │  │
│  │  (utils.py) │   │  (Groq API)     │  │
│  └──────┬──────┘   └────────┬────────┘  │
└─────────┼───────────────────┼───────────┘
          │                   │
          ▼                   ▼
┌──────────────────┐  ┌───────────────────┐
│  Job Description │  │  Portfolio Match  │
│  Extraction      │  │  (ChromaDB)       │
│                  │  │  portfolio.py     │
└──────────────────┘  └───────────────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │  Cold Email Output  │
                   │  (Personalized)     │
                   └─────────────────────┘
```

---

## ✨ Key Features

- 🌐 **Web Scraping** — Automatically extracts job descriptions from any careers page URL
- 🧠 **LLM-Powered** — Uses **Llama 3.1** (open-source) via Groq for fast, high-quality generation
- 🔍 **Semantic Portfolio Matching** — **ChromaDB** vector store matches job requirements to your best portfolio projects
- ✉️ **Personalized Emails** — Generates context-aware cold emails with relevant portfolio links included
- ⚡ **LangChain Chains** — Clean, modular prompt chaining for extraction → matching → generation
- 🖥️ **Streamlit UI** — Simple, user-friendly interface — just paste a URL and get your email
- 🗂️ **CSV Portfolio** — Easily update your portfolio by editing a simple CSV file

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | Llama 3.1 (Meta, open-source) via Groq API |
| LLM Orchestration | LangChain |
| Vector Database | ChromaDB |
| Web Scraping | LangChain WebBaseLoader |
| Frontend | Streamlit |
| Portfolio Data | CSV (`my_portfolio.csv`) |
| Language | Python 3.x |

---

## 📁 Project Structure
```
cold_email_generator/
│
├── main.py               # Streamlit app — main entry point
├── chains.py             # LangChain chains (extraction + email generation)
├── portfolio.py          # ChromaDB vector store + portfolio matching
├── utils.py              # Web scraping & text cleaning utilities
├── my_portfolio.csv      # Your portfolio data (tech stack + project links)
├── .sample.env           # this is the sample shown for using API keys (Groq API key)
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/kruti107/cold_email_generator-.git
cd cold_email_generator-
```

### 2. Install Dependencies
```bash
pip install langchain langchain-community chromadb streamlit groq python-dotenv
```

Or if a `requirements.txt` is present:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Update Your Portfolio

Edit `my_portfolio.csv` to add your own projects and tech stack:
```csv
Tech Stack,Links
Python | Machine Learning | NLP,https://github.com/yourproject1
React | Node.js | REST APIs,https://github.com/yourproject2
LangChain | ChromaDB | LLMs,https://github.com/yourproject3
```

### 5. Run the App
```bash
streamlit run main.py
```

Open your browser at `http://localhost:8501`, paste a job posting URL, and generate your cold email!

---

## 🎯 How to Use

1. **Launch the app** with `streamlit run main.py`
2. **Paste a URL** of a company's job posting or careers page
3. **Click Generate** — the tool scrapes the job, matches your portfolio, and writes the email
4. **Copy the email** and send it directly to the hiring manager or business contact

---

## 📊 Example Output

**Input URL:** `https://jobs.nike.com/job/some-engineering-role`

**Generated Email:**
```
Subject: Helping Nike Scale Engineering Capabilities

Dear Hiring Team,

I came across your opening for a Senior Machine Learning Engineer and wanted 
to reach out. At [Your Company], we specialize in building production-ready 
ML pipelines and have helped companies reduce model deployment time by 40%.

Here are some relevant projects from our portfolio:
- NLP Pipeline for E-commerce: https://github.com/yourproject
- MLOps Automation Framework: https://github.com/yourproject2

I'd love to explore how we can support Nike's engineering goals.

Best regards,
[Your Name]
```

---

## 💼 Why This Project Matters for Recruiters

This project demonstrates a full set of in-demand AI/ML engineering skills:

| Skill | How It's Demonstrated |
|---|---|
| **LLM Integration** | Llama 3.1 via Groq API with LangChain |
| **Prompt Engineering** | Custom chains for structured extraction & generation |
| **Vector Databases** | ChromaDB for semantic portfolio matching |
| **Web Scraping** | Automated job description extraction |
| **End-to-End AI App** | From raw URL → structured data → personalized output |
| **Streamlit Deployment** | Clean, usable frontend — not just a notebook |
| **Modular Code Design** | Separate modules for chains, portfolio, utils |

---

## 🔭 Future Enhancements

- [ ] Add **email tone selector** (formal / casual / aggressive)
- [ ] Support **bulk URL processing** for batch email generation
- [ ] Integrate **Gmail / Outlook API** for one-click sending
- [ ] Add **A/B testing** for email subject lines
- [ ] Build a **job tracking dashboard** to monitor outreach
- [ ] Add **multi-language support** for international outreach

---

## 🌐 Use Cases

- 🏢 **Software & AI Services Companies** — Automated B2B outreach at scale
- 👩‍💻 **Freelancers** — Personalized pitches for every job posting
- 🚀 **Startups** — Fast client acquisition with targeted emails
- 🎓 **Students** — Cold email professors or companies for internships

---

## 👩‍💻 Author

**Kruti**
AI/ML Engineer | LLM Applications | Generative AI

[![GitHub](https://img.shields.io/badge/GitHub-kruti107-black?style=flat&logo=github)](https://github.com/kruti107)

---

## 🙏 Acknowledgements

- 📺 **Tutorial Credit:** [Cold Email Generator — End-to-End LLM Project (YouTube)](https://youtu.be/CO4E_9V6li0) — for the foundational walkthrough and inspiration behind this project
- 🦙 [Meta / Llama 3.1](https://ai.meta.com/llama/) — for the open-source LLM
- ⚡ [Groq](https://groq.com/) — for blazing-fast LLM inference
- 🔗 [LangChain](https://langchain.com/) — for the LLM orchestration framework
- 🗃️ [ChromaDB](https://www.trychroma.com/) — for the vector database
- 🖥️ [Streamlit](https://streamlit.io/) — for the rapid UI framework

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">⭐ If this project helped you learn about LLM applications, please give it a star!</p>
