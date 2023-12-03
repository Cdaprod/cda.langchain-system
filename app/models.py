from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from dataclasses import dataclass

Base = declarative_base()

# Define SQLAlchemy models
class RunnableModel(Base):
    __tablename__ = 'runnables'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    metadata = Column(String)  # Consider using JSON if metadata is complex

# Define dataclasses for your application schemas
@dataclass
class RunnableData:
    name: str
    description: str
    metadata: dict  # Ensure this aligns with how you store metadata in the RunnableModel

# Other models and dataclasses as needed...

# Database setup (adjust as per your configuration)
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create database tables
Base.metadata.create_all(bind=engine)
