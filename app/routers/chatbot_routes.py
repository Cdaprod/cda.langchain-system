from fastapi import APIRouter, HTTPException
from ..utils.conversational_agent import ConversationalAgent

router = APIRouter()
agent = ConversationalAgent()

@router.post("/chat/{bucket_name}")
async def chat_with_agent(bucket_name: str, message: str):
    try:
        response = agent.process_message(message, bucket_name)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
