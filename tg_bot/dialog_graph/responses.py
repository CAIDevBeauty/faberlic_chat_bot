from dff import Context, Pipeline
from dff.script import Message
from . import consts



product_tags = {
    "hair_type": "тип волос",
    "product_type": "тип продукта",
    "price": "цена",
    "series": "серия"
}
def get_welcome_text(ctx: Context, _: Pipeline) -> Message:
    return Message("Вас приветствует бот-консультант Фаберлик! Я отвечу на любой ваш вопрос или помогу сделать заказ")

def get_cannot_extract_all_slots_text(ctx: Context, _: Pipeline) -> Message:
    data = ctx.misc[consts.SLOTS]
    return Message(text=f"Не хватает данных для поиска, пожалуйста, опишите еще {', '.join(product_tags.get(key) for key, value in data.items() if  value is None)}")
