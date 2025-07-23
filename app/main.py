from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="E-commerce AI Agent",
    description="An AI-powered assistant that helps answer data-related queries from e-commerce datasets.",
    version="1.0",
)

app.include_router(router)
