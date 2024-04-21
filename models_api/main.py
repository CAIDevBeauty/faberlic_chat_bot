from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import router
from models.intent_classifier import IntentClassifier
from models.slots_filler import SlotsFiiler


def create_app():
    new_app = FastAPI()
    new_app.include_router(router)
    new_app.state.intent_classifier = IntentClassifier(candidate_labels=["purchase of goods"
        "registration on the site",
        "payment for goods"
        "receipt of goods"
        "product cancellation"
        "purchase returns"])
    new_app.state.slots_filler = SlotsFiiler()
    return new_app


app = create_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)