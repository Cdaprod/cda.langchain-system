from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/bucket/{bucket_name}")
async def get_bucket(bucket_name: str):
    minio_client = get_minio_client()
    try:
        # Retrieve bucket information or contents
        # Example: List objects in the bucket
        objects = minio_client.list_objects(bucket_name)
        object_list = [obj.object_name for obj in objects]
        return {"bucket_name": bucket_name, "objects": object_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving bucket: {e}")
