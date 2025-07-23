import pandas as pd
import sqlite3

# Load CSVs
ad_sales = pd.read_csv("data/ad_sales.csv")
total_sales = pd.read_csv("data/total_sales.csv")
eligibility = pd.read_csv("data/eligibility.csv")

# Clean column names
ad_sales.columns = ad_sales.columns.str.strip()
total_sales.columns = total_sales.columns.str.strip()
eligibility.columns = eligibility.columns.str.strip()

# Connect to SQLite and insert data
conn = sqlite3.connect("ecommerce.db")

ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)
eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)

conn.close()
