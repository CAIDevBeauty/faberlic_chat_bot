from pydantic import BaseModel


class SlotsFillingRequestBody(BaseModel):
    dialog_context: list[str]


class SlotsFillingResponseBody(BaseModel):
    hair_type: str | None = None
    product_type: str | None = None
    price: int | None = None
    series: str | None = None
