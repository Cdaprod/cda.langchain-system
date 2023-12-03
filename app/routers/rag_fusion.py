from fastapi import APIRouter, HTTPException
from ..dependencies import get_minio_client
from ..utils.rag_fusion import execute_rag_fusion_chain

router = APIRouter()

@app.post("/fetch-vectorstore/{bucket_name}")
async def fetch_vectorstore(bucket_name: str, query: str):
    minio_client = get_minio_client()
    try:
        # Logic to fetch vectorstore from the specified bucket
        # and process it using RAG Fusion chain from the notebook
        results = execute_rag_fusion_chain(query, bucket_name, minio_client)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
