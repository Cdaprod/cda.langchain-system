
from fastapi import APIRouter, HTTPException
from ..dependencies import get_minio_client
from ..utils.minio_events import handle_minio_event

router = APIRouter()

@router.post("/process-data-with-minio-lambda/{bucket_name}")
async def process_data_with_minio_lambda(bucket_name: str, object_name: str):
    minio_client = get_minio_client()

    # Triggering the MinIO Object Lambda for specific object processing
    try:
        # Logic to interact with LangChain and MinIO Object Lambda
        # For example, fetching an object from MinIO, processing it, and storing the result
        result = handle_minio_event(bucket_name, object_name, minio_client)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
