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
    """
    Return ChatGPT response if it is coherent, fall back to
    predetermined response otherwise.
    """
    # if ctx.validation:
    #     return Message()
    # responses = ctx.misc[consts.SEARCH_RESULT]
    return TelegramMessage(
        **{
            "text": "Я пример поиска",
            "ui": TelegramUI(
                buttons=[
                    Button(text="19", payload="buy"),
                    Button(text="21", payload="buy"),
                ],
                is_inline=True,
                row_width=1,
            ),
        }
    )
