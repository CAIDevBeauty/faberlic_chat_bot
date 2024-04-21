from pydantic import BaseModel


class IntentRequestBody(BaseModel):
    text: str


class IntentResponseBody(BaseModel):
    intent_class: str
