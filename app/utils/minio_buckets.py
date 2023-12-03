from minio import Minio
from .dependencies import get_minio_client


minio_client = get_minio_client()
# Now, use 'minio_client' to interact with MinIO

# List of buckets to be created
buckets = ["raw_video", "stock_video", "logs", "api", "schemas", "input_data", "output_data", "memory", "chat_history"]

# Create buckets and their master metadata objects
for bucket_name in buckets:
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    
    # Create or update the master metadata object for each bucket
    metadata_object_name = f"{bucket_name}_master_metadata.json"
    # Prepare the metadata content
    metadata_content = {"description": f"Master metadata for {bucket_name}", "contents": []}
    minio_client.put_object(bucket_name, metadata_object_name, metadata_content, len(metadata_content))
