from dff.script import Message
def get_slots(request: Message):
    if not request.text:
        return []
    return {
        "hair_type": "жирные",
        "product_type": "бальзам",
        "price": 400,
    }