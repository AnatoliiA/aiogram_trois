# Created by Kamarali Anatolii at 21:21 30.10.2023 file: echo.py
# проект название aiogramproject
"""
Роутер похоже создается для каждого хендлера
Соотвестно покрываем его декоратором соотвествующего роутера.
"""
from aiogram import types, Router, F
from aiogram.filters import StateFilter, state
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from aiogram.enums import ParseMode
from states import Test

echo_router = Router()


@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message, state: FSMContext):
    text = ["Ехо без стану.", "Повідомлення:", message.text]
    await state.set_state(Test.Q1)
    await message.answer("\n".join(text))


@echo_router.message(F.text)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f"Ехо у стані {hcode(state_name)}",
        "Зміст повідомлення:",
        hcode(message.text),
    ]
    await message.answer("\n".join(text), parse_mode=ParseMode.HTML)
