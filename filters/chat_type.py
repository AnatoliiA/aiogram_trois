# Created by Kamarali Anatolii at 17:54 31.10.2023 file: chat_type.py
# проект название aiogramproject
from typing import Union,  Dict, Any
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



class UserFilter(BaseFilter):
    """Аунтификация пользователя по ID"""

    def __init__(self, access_id: int) -> None:
        self._access_id = access_id

    async def __call__(self, message: Message) -> bool:
        return int(self._access_id) == int(message.chat.id)


class HasLinkFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        # Если entities вообще нет, вернётся None,
        # в этом случае считаем, что это пустой список
        entities = message.entities or []

        # Если есть хотя бы одна ссылка, возвращаем её
        for entity in entities:
            if entity.type == "url":
                return {"link": entity.extract_from(message.text)}

        # Если ничего не нашли, возвращаем None
        return False