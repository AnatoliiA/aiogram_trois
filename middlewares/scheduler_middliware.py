# Created by Kamarali Anatolii at 09:20 02.11.2023 file: scheduler_middliware.py
# проект название latand_project_me

import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from apscheduler_di import ContextSchedulerDecorator


class SchedulerMiddleware(BaseMiddleware):
    '''
         ContextSchedulerDecorator это завернутый в декораторе AsyncIOScheduler
         используется для торого, чтобы передать scheduler в любой хендлер

    '''
    def __init__(self, scheduler: ContextSchedulerDecorator) -> None:
        self.scheduler = scheduler

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        data["scheduler"] = self.scheduler
        return await handler(event, data)
