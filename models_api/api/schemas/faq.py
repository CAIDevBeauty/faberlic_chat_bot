from pydantic  import BaseModel

class FAQRequestBody(BaseModel):
    text: str

class FAQResponseBody(BaseModel):
    answer: str