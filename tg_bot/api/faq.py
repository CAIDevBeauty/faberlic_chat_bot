import requests
from dff.script import Message
import random

SEARCH_SERVICE_URI = "http://localhost:8000/faq/"


def get_answer(request: Message) -> dict | None:
    return "Ответ на вопрос бытия: 42"
