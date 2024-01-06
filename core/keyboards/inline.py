from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook Air 13" M1 2020',
            callback_data="apple_air_13_m1_2020"
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Air 14" M1 2020',
            callback_data="apple_air_14_m1_2020"
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Air 16" M1 2019',
            callback_data="apple_air_16_m1_2019"
        )
    ],
    [
        InlineKeyboardButton(
            text='link',
            url="https://onliner.by"
        )
    ],
    [
        InlineKeyboardButton(
            text='Profile',
            url="tg://user?id=395588506"
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook Air 13" M1 2020',
                            callback_data=MacInfo(model='air', size=13, chip="m1", year=2020))
    keyboard_builder.button(text='Macbook Air 14" M1 2020',
                            callback_data=MacInfo(model='air', size=14, chip="m1", year=2020))
    keyboard_builder.button(text='Macbook Air 16" M1 2019',
                            callback_data=MacInfo(model='air', size=16, chip="m1", year=2019))
    keyboard_builder.button(text='link', url="https://onliner.by")
    keyboard_builder.button(text='Profile', url="tg://user?id=395588506")
    keyboard_builder.adjust(3, 1, 1)
    return keyboard_builder.as_markup()
