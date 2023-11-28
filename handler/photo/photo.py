# Created by Kamarali Anatolii at 11:16 28.11.2023 file: photo.py
# проект название aiogramproject

from aiogram import F
from aiogram.types import Message, PhotoSize, Update
from aiogram import Router, types

# Здесь F - это message
from controller import bot

router_photo =  Router()


@router_photo.message(F.photo)
async def photo_msg(message: Message):
    await message.answer("Это точно какое-то изображение!")