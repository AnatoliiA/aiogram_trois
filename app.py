# Created by Kamarali Anatolii at 19:52 30.10.2023 file: app.py
# проект название aiogramproject
"""
A small `pdoc` example. pdoc.exe
"""
import asyncio
import sys
from aiogram import Bot, Dispatcher

from handler import get_start
from middlewares import CounterMiddleware
from utils import logging


async def main():
    """
    в боте регистрируем роутеы
    1. важно регистрировать middleware нужно ранее чем хендлер
    2. важно есть два способа как регистрировать функцию через
        а) через роутер
        б) через message регистр или соответсвующий update

    """

    from controller import dp, bot
    from handler import routerstart, echo_router

    logging.info("bot start")

    # dp.message.middleware.register(CounterMiddleware())
    dp.message.register(get_start)
    dp.include_router(router=routerstart)
    # dp.message.middleware(CounterMiddleware())
    # dp.include_router(router=router)
    # dp.include_router(router=echo_router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # , stream=sys.stdout)
    asyncio.run(main())
