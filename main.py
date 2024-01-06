from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo, get_hello, get_location
from core.settings import settings
import asyncio
import logging
from core.utils.commands import set_commands
from core.handlers.basic import get_inline
from aiogram.filters import Command
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.middlewares.countermiddlewares import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот остановлен!")


async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s")
    bot = Bot(settings.bots.bot_token, parse_mode="HTML")

    

    dp = Dispatcher()
    dp.message.middleware.register(CounterMiddleware())
    dp.message.middleware.register(OfficeHoursMiddleware())
    # dp.message.register(get_photo, F.photo)
    dp.message.register(get_inline, Command(commands="inline"))
    dp.callback_query.register(select_macbook, MacInfo.filter())
    dp.message.register(get_location, F.content_type == "LOCATION")
    dp.message.register(get_start, F.text == "/start")
    dp.message.register(get_hello, F.text.lower() == "привет")
    dp.message.register(get_photo, F.content_type == 'photo')
    # dp.message.register(get_photo, F.photo)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
