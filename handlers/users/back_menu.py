from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from handlers.users.start import get_kb_menu
from aiogram.types import CallbackQuery


async def cmd_back(call: types.CallbackQuery):
        await call.message.delete()
        await call.message.answer('Ви повернулись у головне меню. Виберить розділ:',reply_markup=get_kb_menu()
                                  )


def register_handler_back(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_back, text="back_menu")
