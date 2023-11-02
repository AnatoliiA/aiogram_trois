# Created by Kamarali Anatolii at 17:54 31.10.2023 file: chat_type.py
# проект название aiogramproject
from typing import Union
from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):  # [1]
    def __init__(self, chat_type: Union[str, list]):  # [2]
        print("f")
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.chat_type, str):
            print(f"{message.chat.type}")
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
