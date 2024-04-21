import abc
from abc import ABCMeta, abstractmethod

from openai import ChatCompletion


class BaseOpenAIModel(metaclass=ABCMeta):
    def __init__(self):
        self._openai_client = ChatCompletion()
    @abstractmethod
    async def get_answer(self, *args, **kwargs):
        pass
