from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from app.sql.run_query import run_query
from app.llm.query_generator import generate_sql

router = APIRouter()

@router.post("/ask")
async def ask_question(request: Request):
    body = await request.json()
    question = body.get("question")

    sql_query = generate_sql(question)
    result = run_query(sql_query, question)

    return StreamingResponse(iter([str(result)]), media_type="text/plain")
