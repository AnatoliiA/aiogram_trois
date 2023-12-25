# Created by Kamarali Anatolii at 13:23 28.11.2023 file: game.py
# проект название aiogramproject
'''
from aiogram.utils.chat_action import ChatActionMiddleware
Это строённый мидлварь ChatActionMiddleware
А можно использовать собственную написанный тогда токен long_operation
идет отуда а ChatActionMiddlewareCustom
flags={"long_operation": "find_location"}
'''
import asyncio
from aiogram import flags
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.chat_action import ChatActionMiddleware
from middlewares import ChatActionMiddlewareCustom, WeekendMessageMiddleware, WeekendCallbackMiddleware



router_game = Router()
router_game.message.filter(F.chat.type == "private")

router_game.message.middleware(WeekendCallbackMiddleware())
router_game.message.middleware(WeekendMessageMiddleware())
router_game.message.middleware(ChatActionMiddleware())


@router_game.message(Command("pass")) # flags={"long_operation": "find_location"}
@flags.chat_action(initial_sleep=2, action="find_location", interval=3)
async def cmd_checkin(message: Message):
    """
    В библиотеке aiogram1 для метода sendChatAction2 доступны следующие статусы:

    typing: для текстовых сообщений
    upload_photo: для фотографий
    record_video или upload_video: для видео
    record_audio или upload_audio: для аудиофайлов
    upload_document: для общих файлов
    find_location: для геолокации
    record_video_note или upload_video_note: для видеозаметок (круглых видео)

    Эти статусы можно использовать в сочетании с классом ChatActionSender,
    который позволяет автоматически отправлять выбранный статус до тех пор,
     пока не выполнится отправка сообщения. Это особенно полезно для долгих операций,
     чтобы пользователи видели, что бот активен и выполняет какую-то работу.
     https://docs.aiogram.dev/en/dev-3.x/utils/chat_action.html
    :param message:
    :type message:
    :return:
    :rtype:
    """
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