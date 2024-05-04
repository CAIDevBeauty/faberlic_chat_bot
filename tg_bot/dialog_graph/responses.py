from dff import Context, Pipeline
from dff.messengers.telegram import TelegramMessage, TelegramUI
from dff.script import Message
from dff.script.core.message import Button

from . import consts

product_tags = {
    "hair_type": "тип волос",
    "product_type": "тип продукта",
    "sex": "пол",
    "is_cheap": "искать подешевле?",
    "action": "действие",
}


def get_welcome_text(ctx: Context, _: Pipeline) -> TelegramMessage:
    return TelegramMessage(
        "Я бот-консультант Фаберлик! Я отвечу на любой ваш вопрос по заказам или помогу сделать заказ"
    )


def get_cannot_extract_all_slots_text(ctx: Context, _: Pipeline) -> Message:
    data = ctx.misc[consts.SLOTS]
    return TelegramMessage(
        text=f"Не хватает данных для поиска, пожалуйста, опишите еще {', '.join(product_tags.get(key) for key, value in data.items() if  value is None)}"
    )


def get_search_result(ctx: Context, _: Pipeline):
    responses = ctx.misc[consts.SEARCH_RESULT]
    buttons = []
    for response in responses:
        buttons.append(Button(text=response["name"], payload="buy"))
    return TelegramMessage(
        **{
            "text": "\n".join([response["answer"] for response in responses]),
            "ui": TelegramUI(buttons=buttons, is_inline=True, row_width=1),
        }
    )


def get_faq_result(ctx: Context, _: Pipeline):
    data = ctx.misc[consts.FAQ_RESULT]
    data = data.replace('\\"', '"')
    return TelegramMessage(parse_mode="HTML", text=data)
