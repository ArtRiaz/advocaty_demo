from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from keyboards.inline import kb_menu, get_kb_menu, get_back
#from data.database import DBCommands, create_db


# db = DBCommands()

bot = Bot


async def cmd_start(message: types.Message):
    with open('libra-picas.png', 'rb') as photo:
#        await create_db()
        await message.answer_photo(
            photo=photo,
            caption=f'<b> Вітаю Вас, {message.from_user.full_name}!\n </b>'
                    f'Ми – юридична фірма EXPATRO, заснована у Києві, яка спеціалізується на наданні послуг іноземним '
                    f'громадянам та компаніям. Ми знаємося на міграційному праві та на правових питаннях, пов’язаних '
                    f'із заснуванням та веденням бізнесу в Україні.'

            , reply_markup=kb_menu())
#        await db.add_new_user()


async def cmd_menu(call: types.CallbackQuery):
    await call.message.answer('Управління меню', reply_markup=get_kb_menu())




def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_callback_query_handler(cmd_menu, text='menu')
