import sqlite3
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

DB_PATH = "ecommerce.db"
STATIC_PATH = "static"

def execute_sql(sql_query: str, question: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if sql_query == "__CHART_CPC__":
        query = """
            SELECT item_id, 
                   ROUND(ad_spend * 1.0 / NULLIF(clicks, 0), 2) AS cpc
            FROM ad_sales
            GROUP BY item_id
            ORDER BY cpc DESC
            LIMIT 5;
        """
        df = pd.read_sql_query(query, conn)

        if not os.path.exists(STATIC_PATH):
            os.makedirs(STATIC_PATH)
        chart_path = os.path.join(STATIC_PATH, "cpc_chart.png")

        plt.figure(figsize=(8, 5))
        plt.bar(df['item_id'].astype(str), df['cpc'], color='orange')
        plt.xlabel("Item ID")
        plt.ylabel("CPC (Cost Per Click)")
        plt.title("Top 5 Products with Highest CPC")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

        top_item = df.iloc[0]
        conn.close()

        return {
            "answer": f"Product ID {top_item['item_id']} had the highest CPC of {top_item['cpc']}.",
            "chart_url": "http://127.0.0.1:8000/static/cpc_chart.png"
        }

    try:
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        return df.to_dict(orient="records")
    except Exception as e:
        conn.close()
        return {"error": str(e)}
