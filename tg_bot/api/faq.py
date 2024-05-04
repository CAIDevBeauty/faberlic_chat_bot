import os

import requests
from dff.script import Message

FAQ_SERVICE_URI = f"{os.getenv('BACKEND_URI')}/faq/"


def get_faq_answer(request: Message) -> str | None:
    if not request.text:
        return None
    request_body = {"text": request.text}
    try:
        response = requests.post(FAQ_SERVICE_URI, json=request_body)
    except requests.RequestException:
        response = None
    if response and response.status_code == 200:
        return response.json()["answer"]
    return None
