import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from cachetools import TTLCache

from utils import THROTTLE_TIME_OTHER, THROTTLE_TIME_SPIN


class ThrottlingMiddleware(BaseMiddleware):
    caches = {
        "spin": TTLCache(maxsize=10_000, ttl=THROTTLE_TIME_SPIN),
        "default": TTLCache(maxsize=10_000, ttl=THROTTLE_TIME_OTHER),
    }

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        logging.info(f"::: {data}")
        throttling_key = get_flag(data, "throttling_key")

        if throttling_key is not None and throttling_key in self.caches:
            if event.chat.id in self.caches[throttling_key]:
                await event.answer("Бот по выходным не работает!", show_alert=True)
                return
            else:
                self.caches[throttling_key][event.chat.id] = None
        return await handler(event, data)


class CounterMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        self.counter += 1
        data["counter"] = self.counter
        logging.info(data["counter"])
        return await handler(event, data)
