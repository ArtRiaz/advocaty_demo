from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import asyncio
from keyboards.inline_question import order


def markup():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='⚖️ Для людей', callback_data='people')
        ],
        [
            InlineKeyboardButton(text='⚖️ Для юридичних осіб', callback_data='phis')
        ],
        [
            InlineKeyboardButton(text="↩️ Назад у головне меню", callback_data='back_menu')
        ]
    ])
    return ikb


async def service(call: types.CallbackQuery):
    with open('a.jpg', 'rb') as photo:
        await call.message.edit_reply_markup()
        await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                  caption=f'<b>Мої послуги</b>\n'
                                          '\n'
                                          f'Працюємо за всіма юридичними напрямками незалежно від складності',
                                  reply_markup=markup())


async def for_people(callback: CallbackQuery):
    await callback.message.answer("<b>Трудові суперечки</b>\n"
                                  "\n"
                                  "Допоможем вам отримати компетентну юридичну консультацію з питань трудового права.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Захист прав споживачів</b>\n"
                                  "\n"
                                  "Ми готові допомогти вам у судовому представництві, в тому числі у справах про "
                                  "неналежну якість товарів та послуг, "
                                  "порушення правил продажу, шахрайства тощо.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Складання заяви, скасування судового наказу</b>\n"
                                  "\n"
                                  f"Забезпечуємо допомогу в складанні заяви та скасуванні судового наказу, а також буду "
                                  "вашим представником у суді та "
                                  "допоможу з необхідними документами.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Сімейні суперечки</b>\n"
                                  "\n"
                                  "Якщо вам потрібна допомога у питаннях розірвання шлюбу, поділу майна, стягненні "
                                  "аліментів або укладанні шлюбного "
                                  "договору, я надаю повний спектр послуг у сімейних правових питаннях, щоб захистити"
                                  " ваші права та інтереси.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Адміністративне судочинство</b>\n"
                                  "\n"
                                  "Захищаєм ваші інтереси в адміністративному суді, надаю допомогу з захисту порушених "
                                  "прав та підготую заперечення на "
                                  "складені протоколи та постанови.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Адвокат у кримінальних справах</b>\n"
                                  "\n"
                                  "Маємо величезний досвід у роботі з найскладнішими справами та готовий допомогти вам "
                                  "захищати ваші інтереси на "
                                  "досудовому слідстві та у суді.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Право на спадщину</b>\n"
                                  "\n"
                                  "Допомагаєм вирішити різні питання, пов'язані зі спадщиною, включаючи складні "
                                  "ситуації з поділом майна між "
                                  "спадкоємцями, суперечки між ними, визнання дійсності заповіту або його оскарження, "
                                  "а також питання, пов'язані з правом на отримання спадщини.",
                                  reply_markup=order())


"""for phisic"""


async def for_phisic(callback: CallbackQuery):
    await callback.message.answer("<b>Бухгалтерське обслуговування</b>\n"
                                  "\n"
                                  "Надаєм послуги з бухгалтерського обліку та податкового консультування. Організую "
                                  "незалежний внутрішній контроль "
                                  "фінансової інформації.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Економічна безпека</b>\n"
                                  "\n"
                                  "Надаєм послуги з економічної безпеки, які включають захист ваших інтересів на досудовому слідстві та у суді. Маю "
                                  "великий досвід у складних справах та готовий допомогти вирішити будь-які проблеми, "
                                  "пов'язані з економічною безпекою вашого бізнесу.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Налогові консультації</b>\n"
                                  "\n"
                                  "Готовий надати вам професійні послуги з налогових консультацій та допомогти вирішити будь-які питання, пов'язані з "
                                  "оподаткуванням.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Абонентське обслуговування</b>\n"
                                  "\n"
                                  "Я можу запропонувати послугу абонентського обслуговування, що включає супровід "
                                  "господарської діяльності вашого "
                                  "підприємства з усіх правових питань.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Складання договорів</b>\n"
                                  "\n"
                                  "Надаєм послуги складання договорів. Це необхідно для правильного ведення бізнесу та "
                                  "успішного укладення угод.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Представництво в судах</b>\n"
                                  "\n"
                                  "Надаєм послуги представництва в судах будь-якого рівня та напрямку: від підготовки "
                                  "документів та розробки стратегії "
                                  "захисту до представництва у суді та захисту ваших інтересів.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Документи для підприємців</b>\n"
                                  "\n"
                                  "Допомагаємо у складанні необхідних документів для вашого бізнесу. Включає в себе "
                                  "документи для розвитку фірми, "
                                  "участі в тендерах.")
    await asyncio.sleep(2)
    await callback.message.answer("<b>Приватне підприємство</b>\n"
                                  "\n"
                                  "Розглядаємо питання, пов'язані з реєстрацієй, змінами, ліквідацієй та банкрутством "
                                  "приватних підприємств. Звертайтесь "
                                  "для отримання професійної консультації та підтримки.", reply_markup=order())


async def inline_cancel_service(call: CallbackQuery):
    with open('a.jpg', 'rb') as photo:
        await call.bot.send_photo(chat_id=call.from_user.id, photo=photo,
                                  caption=f'<b>Наші послуги</b>\n'
                                          '\n'
                                          f'Працюю за всіма юридичними напрямками незалежно від складності',
                                  reply_markup=markup())


def register_service(dp: Dispatcher):
    dp.register_callback_query_handler(service, text="service")
    dp.register_callback_query_handler(for_people, text='people')
    dp.register_callback_query_handler(for_phisic, text='phis')
    dp.register_callback_query_handler(inline_cancel_service, text='cancel_service_people')