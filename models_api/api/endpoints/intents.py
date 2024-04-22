from fastapi import APIRouter, Request

from api.schemas.intents import IntentRequestBody, IntentResponseBody

router = APIRouter()


@router.post(path="/", responses={200: {"model": IntentResponseBody}})
async def get_intents(requests: Request, body: IntentRequestBody) -> IntentResponseBody:
    intent_classifier = requests.app.state.intent_classifier

    result = await intent_classifier.get_answer(body.text)
    return IntentResponseBody(intent_class=result)
