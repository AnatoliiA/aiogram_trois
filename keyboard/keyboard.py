# Created by Kamarali Anatolii at 22:40 30.10.2023 file: keyboard.py
# проект название aiogramproject
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.const import SPIN_TEXT


def get_spin_keyboard():
    keyboard = [[KeyboardButton(text=SPIN_TEXT)]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
