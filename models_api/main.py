from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import router
from models.question_classifier import FAQClassifier


def create_app():
    new_app = FastAPI()
    new_app.include_router(router)
    new_app.state.question_classifier = FAQClassifier()
    return new_app


app = create_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
