from fastapi import FastAPI

from app.core.models import models
from app.core.database.database import engine


app = FastAPI()


@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
