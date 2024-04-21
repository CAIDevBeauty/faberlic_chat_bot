from openai import ChatCompletion
from models.dataclasses import Slots
class SlotsFiiler:
    def __init__(self):
        self._openai_client = ChatCompletion()
    async def get_slots(self, contexts: list[str]) -> Slots:
        completion = await self._openai_client.acreate(
            model="gpt-3.5-turbo",
            functions=[Slots.openai_schema],
            messages=[

                {"role": 'system', "content": "I'm going to ask for slots details. Use Slots to parse this data."},
                 {"role": "user", "content": ". ".join(contexts)},
            ]
        )
        slots_detail = Slots.from_response(completion)
        return slots_detail
