   # Created by Kamarali Anatolii at 09:37 02.11.2023 file: scheduler.py
# проект название aiogramproject
import logging
from aiogram import Router, Bot
from aiogram.types import Message


async def get_start(bot: Bot):
    '''
    :param bot: принимает bot
    :type bot: aiogram.Bot
    :return:
    :rtype:
    '''
    await bot.send_message(5847304479, f"2 message work")
    logging.info("message sent")