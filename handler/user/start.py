# Created by Kamarali Anatolii at 22:39 30.10.2023 file: start.py
# проект название aiogramproject
from textwrap import dedent

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from utils.const import START_POINTS
from keyboard.keyboard import get_spin_keyboard


flags = {"throttling_key": "default"}
router = Router()


@router.message(Command("start"), flags=flags)
async def cmd_start(message: Message, state: FSMContext):
    start_text = """\
    <b>Добро пожаловать в наше виртуальное казино!</b>
    У вас {points} очков. Каждая попытка стоит 1 очко, а за выигрышные комбинации вы получите:

    3 одинаковых символа (кроме семёрки) — 7 очков
    7️⃣7️⃣▫️ — 5 очков (квадрат = что угодно)
    7️⃣7️⃣7️⃣ — 10 очков

    <b>Внимание</b>: бот предназначен исключительно для демонстрации, и ваши данные могут быть сброшены в любой момент! 
    Помните: лудомания — это болезнь, и никаких платных опций в боте нет.

    Убрать клавиатуру — /stop
    Показать клавиатуру, если пропала — /spin
    """
    await state.update_data(score=START_POINTS)
    await message.answer(
        dedent(start_text).format(points=START_POINTS), reply_markup=get_spin_keyboard()
    )


@router.message(Command("stop"), flags=flags)
async def cmd_stop(message: Message):
    await message.answer(
        "Клавиатура удалена. Начать заново: /start, вернуть клавиатуру и продолжить: /spin",
        reply_markup=ReplyKeyboardRemove(),
    )
