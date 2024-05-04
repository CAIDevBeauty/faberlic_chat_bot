from pydantic import BaseModel, Field


class SlotsFillingRequestBody(BaseModel):
    dialog_context: list[str]


class SlotsFillingResponseBody(BaseModel):
    sex: str | None = None
    product_type: str | None = None
    action: str | None = None
    hair_type: str | None = None
    is_cheap: bool | None = None
