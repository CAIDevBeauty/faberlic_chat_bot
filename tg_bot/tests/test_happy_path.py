import pytest
from dff.messengers.telegram import TelegramMessage, TelegramUI
from dff.script.core.message import Button
from dff.utils.testing import check_happy_path

from main import get_pipeline


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "happy_path",
    [
        (
            (
                TelegramMessage(text="/start"),
                TelegramMessage(
                    text="Я бот-консультант Фаберлик! Я отвечу на любой ваш вопрос по заказам или помогу сделать заказ"
                ),
            ),
            (
                TelegramMessage(
                    text="Девушка, 30 лет, порекомендуй шампунь для восстановления окрашенных волос. Самые дешевые товары."
                ),
                TelegramMessage(
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
                ),
            ),
            (
                TelegramMessage(text="Я хочу купить шампунь"),
                TelegramMessage(text="Не хватает данных для поиска, пожалуйста, опишите еще пол, действие, тип волос"),
            ),
            (
                TelegramMessage(text="Женский, для длинных волос, увлажняющий"),
                TelegramMessage(
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
                ),
            ),
            (TelegramMessage(text="Как отменить товар?"), TelegramMessage(text="я отвечаю на faq")),
        )
    ],
)
async def test_happy_path(happy_path):
    check_happy_path(get_pipeline(use_cli_interface=True, use_context_storage=False), happy_path)
