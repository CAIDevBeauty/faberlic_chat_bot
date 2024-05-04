from openai_function_call import OpenAISchema
from pydantic import Field

from models.utils import ACTION, HAIR_TYPE, PRODUCT_TYPE, SEX


class Slots(OpenAISchema):
    hair_type: str | None = Field(default=None, description=f'Тип волос (пример: {",".join(HAIR_TYPE)})')
    product_type: str | None = Field(default=None, description=f'Тип товара (пример: {",".join(PRODUCT_TYPE)})')
    action: str | None = Field(default=None, description=f'Действие (пример: {",".join(ACTION)})')
    sex: str | None = Field(default=None, description=f'Пол (пример: {",".join(SEX)})')
    is_cheap: bool = Field(default=False, description="Нужно ли искать товары подешевле")


class Intent(OpenAISchema):
    intent_name: str | None = Field(default=None, description="Класс интента")
