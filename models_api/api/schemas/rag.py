from pydantic import BaseModel


class RAGRequestBody(BaseModel):
    text: str | None = None
    sex: str | None = None
    product_type: str | None = None
    action: str | None = None
    hair_type: str | None = None
    is_cheap: bool | None = None


class RAGResponseBody(BaseModel):
    answer: str | None = None
    name: str | None = None
    link: str | None = None
