from app.llm.rules import convert_question_to_sql
from app.sql.execute_query import execute_sql

def generate_sql(question: str) -> str:
    return convert_question_to_sql(question)

def execute_sql_wrapper(question: str):
    sql = convert_question_to_sql(question)
    return execute_sql(sql, question)
