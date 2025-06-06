from fastapi import FastAPI
from app.db import engine
from app.models import model
from app.api import api

app = FastAPI(title="Task Manager API")

@app.get("/")
def home():
    return {"message": "API online"}

model.Base.metadata.create_all(bind=engine)

app.include_router(api.router)