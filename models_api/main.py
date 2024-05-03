from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import router
from models.answer_generator import AnswerGenerator
from models.products_retriever import Retriever


def create_app():
    new_app = FastAPI()
    new_app.include_router(router)
    new_app.state.retriever = Retriever("catalog.xlsx")
    new_app.state.answer_generator = AnswerGenerator()
    return new_app


app = create_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
