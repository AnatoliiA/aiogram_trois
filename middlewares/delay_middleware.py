# Created by Kamarali Anatolii at 11:40 28.11.2023 file: delay_middleware.py
# проект название aiogramproject
import asyncio
from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

class SlowpokeMiddleware(BaseMiddleware):
    def __init__(self, sleep_sec: int):
        self.sleep_sec = sleep_sec

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        # Ждём указанное количество секунд и передаём управление дальше по цепочке
        # (это может быть как хэндлер, так и следующая мидлварь)
        print(f"Delaying handler by {self.sleep_sec} seconds")
        # Запускаем цикл, который каждую секунду выводит сообщение о прошедшем времени
        for i in range(self.sleep_sec, 0, -1):
            print(f"Time remaining: {i} seconds")
            await asyncio.sleep(1)

        result = await handler(event, data)
        # Если в хэндлере сделать return, то это значение попадёт в result
        print(f"Handler was delayed by {self.sleep_sec} seconds")
        return result