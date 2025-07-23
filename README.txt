📊 E-commerce AI Agent
An intelligent FastAPI-based assistant that helps users query e-commerce data using natural language. It translates plain questions into SQL and returns accurate results from a local SQLite database — with optional charts for deeper insight.

🚀 Features
* ⚡ FastAPI backend with /ask endpoint
* 🔁 Converts questions into SQL automatically
* 📊 Generates charts for certain queries (e.g., highest CPC)
* 🗃️ Loads raw CSV data into SQLite
* 📤 Streams output like a real assistant
* 🧱 Simple, modular codebase (LLM, SQL, API)

🗂️ Folder Structure
ecommerce-ai-agent/
│
├── app/
│   ├── api/                 # FastAPI endpoints
│   ├── llm/                 # Question-to-SQL logic
│   ├── sql/                 # SQL execution + streaming
│   └── main.py              # App entry point
│
├── data/
│   ├── ad_sales.csv
│   ├── total_sales.csv
│   ├── eligibility.csv
│   └── load_data.py         # Loads CSVs into SQLite
│
├── static/                  # Chart outputs
│   └── cpc_chart.png        # Auto-generated
│
├── ecommerce.db             # Final SQLite database
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Setup Instructions
Requires Python 3.8+
1. Install dependencies
pip install -r requirements.txt
Or manually:
pip install fastapi uvicorn matplotlib pandas
2. Load the database
python data/load_data.py
3. Run the FastAPI server
uvicorn app.main:app --reload
Server: http://127.0.0.1:8000

✅ How to Test:
Option 1: Terminal (curl)
curl -N -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Which product had the highest CPC?"}'
More example questions:
* "What is the total sales made?"
* "Tell me the total sales"
* "Show the top CPC item?"

Option 2: Swagger UI
Visit: http://127.0.0.1:8000/docs Use the /ask endpoint with your question.

📈 Chart Output
When asked: "Which product had the highest CPC?" A bar chart is generated and saved at:
http://127.0.0.1:8000/static/cpc_chart.png

🎯 Why This Structure?
* ✅ No external API calls — everything runs locally
* ✅ Clean modular code — easy to swap components
* ✅ Basic rules + optional LLM fallback if extended
* ✅ Ideal for demo, interview, or GenAI evaluation

📌 Final Notes
* Built as part of a GenAI assignment task
* Focused on clarity, reliability, and real-world application
* Safe SQL: CPC uses NULLIF to avoid divide-by-zero

🙌 Thank You
If you're evaluating this project — thank you for your time. Feel free to explore and test.

