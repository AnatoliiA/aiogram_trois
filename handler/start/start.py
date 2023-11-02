# Created by Kamarali Anatolii at 15:53 31.10.2023 file: start.py
# проект название aiogramproject
"""
    Для того чтобы бот видел проект добавлять бота в проект необходимо админом.
    Иначе бот не видит.
    pdoc.exe
"""
import logging

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command
from aiogram.types import Message

from filters import HasUsernamesFilter
from filters.chat_type import ChatTypeFilter

from aiogram.filters import MagicData
from aiogram import F
from typing import Callable, Dict, Any, Awaitable, List
from middlewares.trottling import CounterMiddleware, ThrottlingMiddleware

routerstart = Router()
# routerstart.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"]))
routerstart.message.middleware.register(CounterMiddleware())


# @dp.message(CommandStart())
# async def command_start_handler(message: Message, data: dict) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     # method automatically or call API method directly via
#     # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
#
#     await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@routerstart.my_chat_member()
async def cmd_dice_chanel_in_group(message: Message, counter: str):
    """
    chat type filter ловит сообщения в групах
    from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER

    @router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
    async def on_user_leave(event: ChatMemberUpdated): ...

    @router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
    async def on_user_join(event: ChatMemberUpdated): ...
    """

    logging.info(message.chat.type)
    await message.answer_dice(emoji=DiceEmoji.DICE)


# Command("dice")
@routerstart.message()
async def cmd_dice_in_group(message: Message, counter: str):
    '''
    :param message:  принимает параметры
    Откуда берется counter это берется из сообтвествующего миддлваря.
    где в массив дата загружается соответствующая функция handler(event, data)
    которая соответствует до хендлера данным которые мы туда положили
        self.counter += 1
        data["counter"] = self.counter
        logging.info(data["counter"])
        return await handler(event, data)
    :type message:
    :param counter:
    :type counter:
    :return:
    :rtype:
    '''
    print(counter)
    await message.answer_dice(emoji=DiceEmoji.DICE)


#
#
# @routerstart.message(Command("basketball"))
# async def cmd_basketball_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.BASKETBALL)
