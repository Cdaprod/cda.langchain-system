from fastapi import APIRouter, HTTPException
from ..dependencies import get_minio_client

router = APIRouter()

@router.get("/list-bucket-contents/{bucket_name}")
async def list_bucket_contents(bucket_name: str):
    minio_client = get_minio_client()  # Get the MinIO client

    try:
        objects = minio_client.list_objects(bucket_name)
        object_names = [obj.object_name for obj in objects]
        return {"bucket_contents": object_names}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))