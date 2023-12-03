from fastapi import APIRouter, HTTPException
from .dependencies import get_minio_client
import json

router = APIRouter()

@router.get("/chat-embeddings/{bucket_name}")
async def get_chat_embeddings(bucket_name: str):
    minio_client = get_minio_client()
    try:
        data = minio_client.get_object(bucket_name, 'chat_embeddings.json').data
        embeddings = json.loads(data)
        return embeddings
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching embeddings: {e}")