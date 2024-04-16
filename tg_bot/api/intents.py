import requests
from dff.script import Message


DNNC_SERVICE = "http://localhost:8080/intents"


def get_intents(request: Message):
    """
    Query the local service extracting intents from the
    last user utterance.
    """
    # if not request.text:
    #     return []
    # request_body = {"dialog_contexts": [request.text]}
    # try:
    #     response = requests.post(DNNC_SERVICE, json=request_body)
    # except requests.RequestException:
    #     response = None
    # if response and response.status_code == 200:
    #     return [response.json()[0][0]]
    # return []
    return ["purchase"]