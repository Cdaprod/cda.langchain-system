from fastapi import FastAPI, BackgroundTasks, HTTPException
from .routers import chatbot_routes, rag_fusion, process_bucket, minio_event, object_operations, bucket_operations
from .models import RunnableModel, SessionLocal
from .utils.feature_store import FeatureStore
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

# Include all your routers
app.include_router(chatbot_routes.router)
app.include_router(rag_fusion.router)
app.include_router(process_bucket.router)
app.include_router(minio_event.router)
app.include_router(object_operations.router)
app.include_router(bucket_operations.router)

class RunnableRequest(BaseModel):
    name: str
    description: str
    metadata: dict

@app.post("/index-runnable/")
async def index_langchain_runnable(runnable_data: RunnableRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(add_runnable_to_feature_store, runnable_data)
    return {"message": "Runnable indexing initiated"}

def add_runnable_to_feature_store(data: RunnableRequest):
    db: Session = SessionLocal()
    try:
        new_runnable = RunnableModel(**data.dict())
        db.add(new_runnable)
        db.commit()
        db.refresh(new_runnable)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    except ValidationError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Validation error: {e}")
    finally:
        db.close()