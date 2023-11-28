# Created by Kamarali Anatolii at 16:23 28.11.2023 file: longoperation.py
# проект название aiogramproject
from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender
from typing import Any, Callable, Dict, Awaitable
from aiogram.types import Message


class ChatActionMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        from controller import bot
        long_operation_type = get_flag(data, "long_operation")

        # Если такого флага на хэндлере нет
        if not long_operation_type:
            return await handler(event, data)

        # Если флаг есть
        async with ChatActionSender(
                bot=bot,
                action=long_operation_type,
                chat_id=event.chat.id):
            return await handler(event, data)
