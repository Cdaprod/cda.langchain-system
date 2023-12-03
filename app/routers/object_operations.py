from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/bucket/{bucket_name}/object/{object_name}")
async def get_object(bucket_name: str, object_name: str):
    minio_client = get_minio_client()
    try:
        object_data = minio_client.get_object(bucket_name, object_name).data
        return {"object_name": object_name, "data": object_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving object: {e}")

