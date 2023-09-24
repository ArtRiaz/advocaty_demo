from aiogram.types import CallbackQuery
from aiogram import Dispatcher
from keyboards.inline import get_back
from aiogram import types, Dispatcher
from keyboards.inline_question import ikb_question, back_quest
from aiogram.dispatcher.filters import Text


async def questions(call: types.CallbackQuery):
    with open('a.jpg', 'rb') as photo:
        await call.message.edit_reply_markup()
        await call.bot.send_photo(chat_id=call.from_user.id, photo=photo)
        await call.message.answer("Відповіді на ваші запитання:", reply_markup=ikb_question())


async def question_1(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("- Погодинна оплата- оплата за робочі години адвоката, які витрачені на виконання "
                                  "завдання клієнта\n "
                                  "- Фіксований гонорар. Фіксована оплата на весь термін співробітництва та повного "
                                  "ведення справи, яка не залежить від "
                                  "обсягу роботи, кількості судових засідань та інших факторів\n "
                                  "- “Гонорар успіху”. Коли оплата проводиться за результатом, який обумовлюється "
                                  "клієнтом і оплачується лише у разі "
                                  "досягнення позитивного результату для клієнта. Важливо розуміти, що гонорар успіху "
                                  "завжди буде вищим, ніж у разі фіксованої оплати.",
                                  reply_markup=back_quest())


async def question_2(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Звичайно! Це один з найважливіших принципів моєї роботи - повна інформаційна "
                                  "прозорість перед клієнтом щодо прогресу справи та виконаної роботи, "
                                  "при цьому остаточне рішення про подальші дії завжди залишається клієнту. Я вказую "
                                  "на можливі варіанти і кроки, щоб разом вибрати найвідповідніший варіант для "
                                  "клієнта.",
                                  reply_markup=back_quest())


async def question_3(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Адвокат не може представляти одночасно кілька сторін, які мають протилежні "
                                  "інтереси. Адвокат може тільки допомагати у досягненні мирного врегулювання "
                                  "суперечок. Тому, працюючи зі мною, ви можете бути впевнені, що я не буду "
                                  "представляти інтереси інших сторін, які можуть перешкодити досягненню вашої мети.",
                                  reply_markup=back_quest())


async def question_4(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("- Забезпечення уваги до деталей та уникнення помилок на початковій стадії "
                                  "проблемної ситуації, коли перспективи рішення (включаючи судові) багато в чому "
                                  "визначені\n "
                                  "- Оцінювання судових перспектив справи та ризиків різних рішень, пропонування "
                                  "клієнту варіантів дій для досягнення "
                                  "найбільш сприятливого розв'язання конкретної ситуації\n "
                                  "- Захист прав клієнта за всіма законними засобами в судових та правоохоронних "
                                  "органах",
                                  reply_markup=back_quest())


async def question_5(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Так, це можливо! У випадку послуги передплати укладається відповідний договір, "
                                  "за яким здійснюється фіксована щомісячна оплата і обумовлюється відповідний пакет "
                                  "послуг, шляхом передплати заздалегідь визначеної кількості годин на "
                                  "місяць/півріччя/рік",
                                  reply_markup=back_quest())


async def inline_cancel(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Відміна", reply_markup=ikb_question())


def question_menu(dp: Dispatcher):
    dp.register_callback_query_handler(questions, text='questions')
    dp.register_callback_query_handler(question_1, text='1')
    dp.register_callback_query_handler(question_2, text='2')
    dp.register_callback_query_handler(question_3, text='3')
    dp.register_callback_query_handler(question_4, text='4')
    dp.register_callback_query_handler(question_4, text='5')
    dp.register_callback_query_handler(inline_cancel, text='cancel')
