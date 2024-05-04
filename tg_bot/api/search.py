import os

import requests
from dff.script import Message

SEARCH_SERVICE_URI = f"{os.getenv('BACKEND_URI')}/rag/"


def search_products(request: Message, search_params) -> dict | None:
    if not request.text:
        return None
    request_body = {"text": request.text, **search_params}
    try:
        response = requests.post(SEARCH_SERVICE_URI, json=request_body)
    except requests.RequestException:
        response = None
    if response and response.status_code == 200:
        return response.json()
    return None
