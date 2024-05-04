from fastapi import APIRouter, Request

from api.schemas.faq import FAQRequestBody, FAQResponseBody

router = APIRouter()


@router.post(path="/", responses={200: {"model": FAQResponseBody}})
async def get_faq_answer(requests: Request, body: FAQRequestBody) -> FAQResponseBody:
    question_classifier = requests.app.state.question_classifier

    result = question_classifier.classify_question(body.text)

    return FAQResponseBody(answer=result)
