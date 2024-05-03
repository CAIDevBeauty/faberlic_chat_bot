from models.base_openai_model import BaseOpenAIModel


class IntentClassifier(BaseOpenAIModel):
    def __init__(self, candidate_labels):
        super().__init__()
        self._candidate_labels = candidate_labels

    async def get_answer(self, text) -> str:
        completion = await self._openai_client.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"I'm going to ask for classify text. Choose one of the classes: [{','.join(self._candidate_labels)}]",
                },
                {"role": "user", "content": text},
            ],
        )
        return completion.choices[0].message["content"]
