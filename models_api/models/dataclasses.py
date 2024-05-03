from openai_function_call import OpenAISchema
from pydantic import Field


class Slots(OpenAISchema):
    hair_type: str | None = Field(default=None, description="Тип волос (пример: жирные, сухие, нормальные)")
    product_type: str | None = Field(default=None, description="Тип товара (пример: шампунь или бальзам")
    price: int | None = Field(default=None, description="Цена товара")
    series: str | None = Field(default=None, description="Линейка или серия товара")


class Intent(OpenAISchema):
    intent_name: str
