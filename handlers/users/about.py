from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from keyboards.inline import get_back


async def about(call: types.CallbackQuery):
    with open('b.jpg', 'rb') as photo1:
        await call.message.edit_reply_markup()
        await call.bot.send_photo(chat_id=call.from_user.id,
                                  photo=photo1,
                                  caption=f"<b>Давайте знайомитись!\n"
                                          "\n"
                                          'EXPATPRO — провідна юридична фірма - бутік, яка фокусується на '
                                          'міграційному праві в Україні та пропонує'
                                          'індивідуальні юридичні послуги найвищої якості для експатів.Коло наших '
                                          'клієнтів включає приватних осіб, підприємства'
                                          'та інвесторів, які  шукають особисті, підприємницькі та трудові можливості '
                                          'в Україні.Наші міграційні експерти'
                                          'мають надзвичайний досвід у правовій, політичній та бізнес сферах, '
                                          'що допоможе провести вас через заплутаний'
                                          'світ українського законодавства.Наша команда надає професійні юридичні '
                                          'поради щодо того, як переїхати, облаштуватись'
                                          'в Україні та розпочати власну справу в Україні у найлегший спосіб та '
                                          'відповідно до законодавства України.</b>', reply_markup=get_back()
                                  )



def register_handlers_about(dp: Dispatcher):
    dp.register_callback_query_handler(about, text="about")
