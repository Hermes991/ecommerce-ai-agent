def convert_question_to_sql(question: str) -> str:
    q = question.lower().strip()

    if "total sales" in q:
        return "SELECT SUM(total_sales) AS total_sales FROM total_sales;"

    if "highest cpc" in q or "top cpc" in q or "most expensive click" in q:
        return "__CHART_CPC__"

    return "SELECT 'Query not understood';"
