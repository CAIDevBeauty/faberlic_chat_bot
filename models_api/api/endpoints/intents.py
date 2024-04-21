from fastapi import APIRouter, Request

from api.schemas.intents import IntentRequestBody, IntentResponseBody

router = APIRouter()


@router.post(path="/", responses={200: {"model": IntentResponseBody}})
async def get_intents(requests: Request, body: IntentRequestBody) -> IntentResponseBody:
    intent_classifier = requests.app.state.intent_classifier

    result = intent_classifier.get_intents(body.text)
    return IntentResponseBody(**result)
