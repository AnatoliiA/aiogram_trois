# Created by Kamarali Anatolii at 11:44 28.11.2023 file: stoke_middleware.py
# проект название aiogramproject
from aiogram import Router
from aiogram.enums import DiceEmoji
from aiogram.filters import Command
from middlewares import SlowpokeMiddleware
from aiogram.types import Message

# Где-то в другом месте
router1 = Router()
router2 = Router()

router1.message.middleware(SlowpokeMiddleware(sleep_sec=5))
router2.message.middleware(SlowpokeMiddleware(sleep_sec=10))

@router1.message(Command("basketball"))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)

@router1.message(Command("ball"))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)