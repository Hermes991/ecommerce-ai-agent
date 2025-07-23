<h1 align="center">🛍️ E-commerce AI Agent</h1>

<p align="center">
  <i>An intelligent assistant that answers natural language questions using SQL on e-commerce data.<br>
  Powered by FastAPI, SQLite, and clean rule-based logic — with optional chart generation.</i>
</p>

---

## Features

- FastAPI backend with a single `/ask` endpoint
- Natural language → SQL translation
- Chart support for specific queries (e.g., highest CPC)
- SQLite backend from raw CSV files
- Streaming assistant-like output
- Clean modular codebase (LLM, SQL, API)

---

## 🗂️ Project Structure

```
ecommerce-ai-agent/
│
├── app/
│   ├── api/          # FastAPI endpoints
│   ├── llm/          # Question-to-SQL logic
│   ├── sql/          # SQL execution + streaming
│   └── main.py       # App entry point
│
├── data/
│   ├── ad_sales.csv
│   ├── total_sales.csv
│   ├── eligibility.csv
│   └── load_data.py  # Loads CSVs into SQLite
│
├── static/           # Chart outputs
│   └── cpc_chart.png # Auto-generated chart
│
├── ecommerce.db      # Final SQLite database
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

> ✅ Requires **Python 3.8+**

### 1. **Install dependencies**
```bash
pip install -r requirements.txt
```

### 2. **(Optional) Install manually if needed:**
```bash
pip install fastapi uvicorn matplotlib pandas
```

### 3. **Load database with CSV data**
```bash
python data/load_data.py
```

### 4. **Run FastAPI server**
```bash
uvicorn app.main:app --reload
```

**Visit your app at:** http://127.0.0.1:8000

---

## Example Questions to Try

### Using curl (Terminal)
```bash
curl -N -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the total sales made?"}'
```

```bash
curl -N -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Calculate the RoAS (Return on Ad Spend)"}'
```

```bash
curl -N -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Which product had the highest CPC?"}'
```

### Demo Questions:
- 1. "What is the total sales made?"
- 2. "Calculate the RoAS (Return on Ad Spend)"
- 3. "Show me the top CPC item"

### Or via Swagger UI
Try the `/ask` endpoint directly from:
**http://127.0.0.1:8000/docs**

---

## 📊 Chart Output Example

When you ask: **"Which product had the highest CPC?"**,
a bar chart is generated at:

📍 **http://127.0.0.1:8000/static/cpc_chart.png**

---

## Why This Project

- **100% local** — no external APIs used
- **LLM-like intelligence** without full models
- **Safe SQL** (NULLIF to avoid divide-by-zero in CPC)
- **Beginner-readable** and modular code
- **Fast to run**, easy to extend

---

##  Use Cases

| Use Case | Example |
|----------|---------|
| **Total Sales** | "What is the total sales made?" |
| **Highest CPC** | "Show me the top CPC product" |
| **Eligibility Breakdown** | "Count eligible items" |

---

## Thank You

This project was built as part of a **GenAI assignment for Anarix**.

If you're evaluating this repo — thank you for your time.
It's designed to reflect **clarity**, **real-world relevance**, and a **creative personal touch**.

---

<p align="center">
  <i>Built by Hermes Deena — July 2025</i>
</p>
```