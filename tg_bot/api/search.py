import requests
from dff.script import Message
import random

SEARCH_SERVICE_URI = "http://localhost:8000/search/"


def search_product(request: Message) -> dict | None:
    i = random.randint(0, 1)
    if i == 1:
        return "Мы нашли следующий продукт: продукт_нейм. Желаете совершить покупку?"
    else:
        return "Мы не нашли ничего, удовлетворяющее вашему запросу. Пожалуйста, попробуйте другие данные"
