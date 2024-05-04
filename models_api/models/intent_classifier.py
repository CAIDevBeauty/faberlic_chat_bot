from models.base_openai_model import BaseOpenAIModel


class IntentClassifier(BaseOpenAIModel):
    async def get_answer(self, text) -> str:
        completion = await self._openai_client.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"I'm going to ask for classify text. Choose one of the classes: [покупка товара, регистрация на сайте, faq]. Predict only class name.",
                },
                {"role": "user", "content": text},
            ],
        )
        return completion.choices[0].message["content"]
