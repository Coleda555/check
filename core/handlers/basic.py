from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tell_pull_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard


async def get_inline(message:Message, bot:Bot):
    await message.answer(f"Привет, {message.from_user.first_name}! \n показываем модели Macbook",
                         reply_markup=get_inline_keyboard())
async def get_start(message: Message, bot: Bot, counter:str):
    await message.answer(f"Сообщение №{counter}")
    await bot.send_message(message.from_user.id,
                           f"<b>Hello, {message.from_user.first_name}! \n </b>"
                           f"<tg-spoiler>your ID {message.from_user.id} \n</tg-spoiler>"
                           f"Добро пожаловать в гробницу автомехаников!",
                           reply_markup=get_reply_keyboard())


async def get_location(message: Message, bot: Bot):  
    await message.answer(f"Ты отправил локацию \r\n"
                         f"{message.location.latitude}\r\n{message.location.longitude}")
    # await message.answer(
    #     f"<tg-spoiler>Hello, {message.from_user.first_name}. Добро пожаловать в гробницу автомехаников!</tg-spoiler>")
    # await message.reply(f"Hello, {message.from_user.first_name}. Добро пожаловать в гробницу автомехаников!")


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Отлично, ты отправил фото обстановки! Я закину его в архив.")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, f"C:/Users/SkyWalker69/PycharmProjects/garage_911/photos/photo.jpg")


async def get_hello(message: Message, bot: Bot):
    await message.answer(f"И тебе привет, {message.from_user.first_name}!")
