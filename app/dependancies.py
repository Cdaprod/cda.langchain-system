import weaviate
import os
from dotenv import load_dotenv
from minio import Minio

load_dotenv()

def get_minio_client() -> Minio:
    return Minio(os.getenv('MINIO_ENDPOINT'),
                 access_key=os.getenv('MINIO_ACCESS_KEY'),
                 secret_key=os.getenv('MINIO_SECRET_KEY'),
                 secure=False)

def get_weaviate_client():
    client = weaviate.WeaviateClient(
        connection_params=weaviate.ConnectionParams(
            http_host="192.168.0.25",  # Your Weaviate host
            http_port="8080",  # Default Weaviate HTTP port
            http_secure=False  # Set to False for non-HTTPS
        ),
        auth_client_secret=weaviate.AuthApiKey(os.getenv("WEAVIATE_APIKEY")),
        additional_headers={"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}
    )
    return client

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")  # Ensure the environment variable is correctly set
