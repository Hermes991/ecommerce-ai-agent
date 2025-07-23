from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 
from app.api.routes import router

app = FastAPI(
    title="E-commerce AI Agent",
    description="An AI-powered assistant that helps answer data-related queries from e-commerce datasets.",
    version="1.0",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce AI Agent API"}
