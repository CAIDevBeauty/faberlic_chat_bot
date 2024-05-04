from pydantic  import BaseModel

class RAGRequestBody(BaseModel):
    text: str | None = None
    sex: str | None = None
    product_type: str | None = None
    action: str | None = None
    hair_type: str | None = None
    is_cheap: bool | None = None

class RAGResponseBody(BaseModel):
    answer_1: str | None = None
    name_1: str | None = None
    link_1: str | None = None
    answer_2: str | None = None
    name_2: str | None = None
    link_2: str | None = None
    answer_3: str | None = None
    name_3: str | None = None
    link_3: str | None = None
