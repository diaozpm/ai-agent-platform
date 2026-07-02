from fastapi import APIRouter

from backend.schemas.chat import ChatRequest
from backend.services import chat_service
router=APIRouter()
@router.post("/chat")
async def chat(request:ChatRequest):
    answer=chat_service.chat(request.message)
    return{
        "answer":answer
    }