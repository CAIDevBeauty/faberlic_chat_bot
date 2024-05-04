import os

import requests
from dff.script import Message

INTENT_RECOGNITION_SERVICE = f"{os.getenv('BACKEND_URI')}/intents/"


def get_intents(request: Message) -> str | None:
    if not request.text:
        return None
    request_body = {"text": request.text}
    try:
        response = requests.post(INTENT_RECOGNITION_SERVICE, json=request_body)
    except requests.RequestException:
        response = None
    if response and response.status_code == 200:
        return response.json()["intent_class"]
    return None
