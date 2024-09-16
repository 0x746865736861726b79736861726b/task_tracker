from fastapi import FastAPI

from app.core.models import models
from app.core.database.database import engine
from app.tracker.user.presentation.routes.user_routes import user_router

app = FastAPI()

app.include_router(user_router)


@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
