from fastapi import APIRouter, Request

from api.schemas.rag import RAGRequestBody, RAGResponseBody

router = APIRouter()


@router.post(path="/", responses={200: {"model": list[RAGResponseBody]}})
async def get_rag_answer(requests: Request, body: RAGRequestBody) -> list[RAGResponseBody]:
    retriever = requests.app.state.retriever
    generator = requests.app.state.answer_generator

    retrieve_results = retriever.get_products_descriptions(body)

    results = list()
    for i, result in enumerate(retrieve_results):
        if result["name"] is not None:
            results.append(
                RAGResponseBody(
                    name=result["name"],
                    link=result["link"],
                    answer=await generator.get_answer(body.text, result["description"]),
                )
            )

    return results
