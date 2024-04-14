from pydantic import BaseModel


class IntentRequestBody(BaseModel):
    text: str


class IntentResponseBody(BaseModel):
    sequence: str
    labels: list[str]
    scores: list[float]
