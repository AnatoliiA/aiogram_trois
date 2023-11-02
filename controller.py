# Created by Kamarali Anatolii at 15:59 31.10.2023 file: controller.py
# проект название aiogramproject
import asyncio

from aiogram import Dispatcher, Bot

from data.config import BOT_TOKEN
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator
from datetime import datetime, timedelta

from handler import get_start


def pr():
    print("test")


def start_redis():
    '''
    :return: Возвращеет в бот storege
    :rtype:
    Redis server рабатает на сторене Ubuntu через wsl
    '''
    from aiogram.fsm.storage.redis import RedisStorage
    return RedisStorage.from_url("redis://127.0.0.1:6379/0")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=start_redis())  # storage=start_redis()

jobstores = {
    "default": RedisJobStore(jobs_key="dispatched_trips_jobs",
                             run_times_key="dispatched_trips_running",
                             host="localhost",
                             db=2,
                             port=6379,
                             pickle_protocol=0)
}


def scheduler(func):
    """
    :param func: функция скедлера принимает функции
    :type func:
    :return:
    :rtype: None
    apscheduler не поддерживает внедрение зависмостей используется декоратор из аpscheduler_di
    redis забирает состаяние работы и после это нужно очищать для того чтобы что работало:
    redis-cli flushall async
    redis-cli flushall
    Cобытия add_job имеют по крайней мере 3 известных тригера:
    date -- конкретная разовая отпрвка
    cron срок - в часах
    interval передает с заданным интервалом
    Есть два способа передачи Bot через кварги и контект
    не проверял но думаю работают идентино
    к каждом заданию маожно добавить id и по нему удалять задание
    """

    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone='Europe/Zurich', jobstores=jobstores))
    # scheduler = AsyncIOScheduler(timezone='UTC')
    # scheduler.remove_job('id123')
    scheduler.ctx.add_instance(bot, declared_class=Bot)
    scheduler.add_job(get_start, trigger="date", replace_existing=True, run_date=datetime.now() + timedelta(seconds=1))
    # scheduler.add_job(get_start, trigger="cron", hour=11, minute=59, kwargs={"bot": bot})
    # scheduler.add_job(get_start, trigger="interval", seconds=4)
    # scheduler.add_job(pr, trigger='interval', seconds=2)

    scheduler.start()

''' асинхронно данная функция не работает'''
scheduler(get_start)
