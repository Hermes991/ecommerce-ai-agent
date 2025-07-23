def convert_question_to_sql(question: str) -> str:
    q = question.lower().strip()

    if "total sales" in q:
        return "SELECT SUM(total_sales) AS total_sales FROM total_sales;"

    if "highest cpc" in q or "top cpc" in q or "most expensive click" in q:
        return "__CHART_CPC__"

    if "roas" in q or "return on ad spend" in q:
        return """
            SELECT 
                ROUND(SUM(total_sales.total_sales) * 1.0 / NULLIF(SUM(ad_sales.ad_spend), 0), 2) AS roas
            FROM 
                total_sales
            JOIN 
                ad_sales ON total_sales.item_id = ad_sales.item_id;
        """

    return "SELECT 'Query not understood';"
