from fastapi import FastAPI

from backend.api.chat import router as chat_router

app=FastAPI(
    title="AI Agent Platform",
    version="0.1.0"
)
@app.get("/")
async def root():
 return {
     "message":"Hello AI Agent"
 }
app.include_router(chat_router)