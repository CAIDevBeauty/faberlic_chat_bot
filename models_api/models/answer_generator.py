from models.base_openai_model import BaseOpenAIModel


class AnswerGenerator(BaseOpenAIModel):
    def __init__(self):
        super().__init__()

    async def get_answer(self, text, products_description) -> str:
        grouped_text = f"Запрос клиента: {text}\nОписание товара:\n{products_description}"
        completion = await self._openai_client.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Ты - консультант магазина косметики в отделе ухода за волосами. Используя описание товара и запрос клиента порекомендуй клиенту товар. Ничего не придумывай, используй только предоставленную информацию. Сделай рекомендацию короткой.",
                },
                {"role": "user", "content": grouped_text},
            ],
        )
        return completion.choices[0].message["content"]
