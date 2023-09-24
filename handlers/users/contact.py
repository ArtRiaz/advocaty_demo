from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.inline_question import ikb_contact
from keyboards.inline_question import back_contact
from aiogram.types import CallbackQuery


async def inline_cancel_contact(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("📞 Виберіть мережу або номер телефону:", reply_markup=ikb_contact())

async def cmd_contact(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('📞 Виберіть мережу або номер телефону:', reply_markup=ikb_contact())


async def send_geo(callback: CallbackQuery):
    await callback.message.delete()
    await callback.bot.send_location(chat_id=callback.from_user.id,
                                     latitude=50.4591598,
                                     longitude=30.5132541,
                                     reply_markup=back_contact()
                                     )


async def send_phone(callback: CallbackQuery):
    await callback.message.delete()
    await callback.bot.send_contact(chat_id=callback.from_user.id,
                                    phone_number='+38 044 339 9881',
                                    first_name='EXPATPRO',
                                    reply_markup=back_contact())


def register_handler_contact(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_contact, text="contact")
    dp.register_callback_query_handler(send_geo, text='Геолокация')
    dp.register_callback_query_handler(send_phone, text='Вызов')
    dp.register_callback_query_handler(inline_cancel_contact, text='cancel_contact')
