import os

import requests
from dff.script import Message

SLOTS_FILLING_SERVICE = f"{os.getenv('BACKEND_URI')}/slots/"


def get_slots(request: Message) -> dict | None:
    if not request.text:
        return None
    request_body = {"dialog_context": [request.text]}
    try:
        response = requests.post(SLOTS_FILLING_SERVICE, json=request_body)
    except requests.RequestException:
        response = None
    if response and response.status_code == 200:
        return response.json()
    return None
