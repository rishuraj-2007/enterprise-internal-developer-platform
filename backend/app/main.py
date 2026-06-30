from fastapi import FastAPI

from app.db.database import Base, engine
from app.models import User

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise Internal Developer Platform API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Enterprise Internal Developer Platform API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}