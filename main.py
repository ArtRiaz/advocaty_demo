import asyncio
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers.users import start, services, back_menu, contact, about, questions, regitster
import create_bot
from create_bot import load_config
from aiogram import Bot, Dispatcher
from middleware.anti_time import Anti_time
from utils.set_commands import set_commands
from aiogram import types

logger = logging.getLogger(__name__)

config = load_config()


def register_all_middleware(dp):
    dp.setup_middleware(Anti_time())


def register_all_handlers(dp):
    start.register_handlers_start(dp)
    services.register_service(dp)
    back_menu.register_handler_back(dp)
    contact.register_handler_contact(dp)
    about.register_handlers_about(dp)
    questions.question_menu(dp)
    regitster.handlers_form(dp)


async def startup(bot: Bot):
    await set_commands(bot)
    await bot.send_message(chat_id=config.tg_bot.admin_ids, text='Бот запущен')


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s'
    )

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config  # доставать config из переменной bot, если в handler я хочу достать что то из Config
    # я делаю => bot.get("config")

    register_all_middleware(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await dp.bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stop")
