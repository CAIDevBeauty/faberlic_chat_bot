from fastapi import APIRouter, Request

from api.schemas.slots import SlotsFillingRequestBody, SlotsFillingResponseBody

router = APIRouter()


@router.post(path="/", responses={200: {"model": SlotsFillingResponseBody}})
async def get_intents(requests: Request, body: SlotsFillingRequestBody) -> SlotsFillingResponseBody:
    slots_filler = requests.app.state.slots_filler

    result = await slots_filler.get_answer(body.dialog_context)
    return result
