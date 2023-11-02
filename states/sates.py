from aiogram import Dispatcher

# Создаем группу состояний Test - для тестирования.
# Если у вас другой смысл состояний - называйте соответственно, не надо тупо копировать Test
from aiogram.fsm.state import State, StatesGroup


class Test(StatesGroup):
    # Создаем состояние в этой группе. Называйте каждое состояние соответственно его назначению.
    # В данном случае Q1 - question 1, то есть первый вопрос. У вас это может быть по-другому
    Q1 = State()
    Q2 = State()
    Q3 = State()
