from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('👨🏼‍💻 Наш сайт', url='https://www.expatpro.co/')
    ], [InlineKeyboardButton('📧 ryslanrey76@gmail.com', url='expatpro@gmail.com')], [
        InlineKeyboardButton('📍 Геолокація', callback_data='Геолокация')
    ], [
        InlineKeyboardButton('☎️ Контактний номер', callback_data='Вызов')
    ],
        [
            InlineKeyboardButton("↩️ Назад у головне меню", callback_data='back_menu')
        ]
    ])

    return ikb


def ikb_question():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('⚖️ Як визначається гонорар адвоката?', callback_data="1")
    ], [InlineKeyboardButton('⚖️ Чи інформуватимуть мене про хід справи?', callback_data="2")], [
        InlineKeyboardButton('⚖️ Що таке конфлікт інтересів?', callback_data="3")
    ], [
        InlineKeyboardButton("⚖️ Що виконувати адвокат у процесі співпраці?", callback_data="4")
    ], [
        InlineKeyboardButton("⚖️ Чи можливе абонентське обслуговування?", callback_data="5")
    ], [
        InlineKeyboardButton("↩️ Назад у головне меню", callback_data="back_menu")
    ]])

    return ikb


def back_quest():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('↩️ Назад', callback_data="cancel")
    ]])

    return ikb


def back_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('↩️ Назад', callback_data="cancel_contact")
    ]])

    return ikb


def order():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('⚖️ Замовити консультацію', callback_data="consultasion")
    ],
        [
            InlineKeyboardButton("↩️ Назад", callback_data="cancel_service_people")
        ]])

    return ikb


def back_admin_panel():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('↩️ Назад', callback_data="cancel_admin_menu")
    ]])

    return ikb
