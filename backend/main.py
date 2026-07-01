from fastapi import FastAPI
app=FastAPI(
    title="AI Agent Platform",
    version="0.1.0"
)
@app.get("/")
async def root():
 return {
     "message":"Hello AI Agent"
 }