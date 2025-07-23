from app.sql.execute_query import execute_sql

def run_query(sql_query: str, question: str = ""):
    return execute_sql(sql_query, question)
