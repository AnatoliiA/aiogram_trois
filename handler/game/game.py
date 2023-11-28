# Created by Kamarali Anatolii at 13:23 28.11.2023 file: game.py
# проект название aiogramproject
import asyncio
from aiogram import flags
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from middlewares import WeekendMessageMiddleware, WeekendCallbackMiddleware



router_game = Router()
router_game.message.filter(F.chat.type == "private")

router_game.message.middleware(WeekendCallbackMiddleware())
router_game.message.middleware(WeekendMessageMiddleware())

@flags.chat_action
@router_game.message(Command("pass")) # flags={"long_operation": "find_location"}
async def cmd_checkin(message: Message):
    for i in range(10, 0, -1):
        print(f"Time remaining: {i} seconds")
        await asyncio.sleep(1)
    await message.answer(
        "Пожалуйста, нажмите на кнопку ниже:",
    )


@router_game.callback_query(F.data == "confirm")
async def checkin_confirm(callback: CallbackQuery):
    await callback.answer(
        "Спасибо, подтверждено!",
        show_alert=True
    )