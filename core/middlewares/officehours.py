from datetime import datetime
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message


def office_hours() -> bool:
    return datetime.now().weekday() in [0, 1, 2, 3, 4] and datetime.now().hour in [i for i in range(8, 19)]


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]

    ) -> Any:
        if office_hours():
            return await handler(event, data)
        else:
            return event.answer(f"Бот не работает. Время работы бота пн-пт с 8:00 до 18:00")
