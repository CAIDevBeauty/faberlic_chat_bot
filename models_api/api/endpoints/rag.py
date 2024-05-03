from fastapi import APIRouter, Request

from api.schemas.rag import RAGRequestBody, RAGResponseBody

router = APIRouter()


@router.post(path="/", responses={200: {"model": RAGResponseBody}})
async def get_rag_answer(requests: Request, body: RAGRequestBody) -> RAGResponseBody:
    retriever = requests.app.state.retriever
    generator = requests.app.state.answer_generator

    retrieve_results = retriever.get_products_descriptions(body)

    results = dict()

    for i, result in enumerate(retrieve_results):
        if result["name"] is not None:
            results[f"name_{i+1}"] = result["name"]
            results[f"link_{i+1}"] = result["link"]
            results[f"answer_{i+1}"] = await generator.get_answer(body.text, result["description"])

    return RAGResponseBody.model_validate(results)