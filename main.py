import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.set_menu import set_main_menu


# Configuration and running
async def main():
    # load config
    config: Config = load_config()

    # init bot & dispatcher
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    # menu register
    await set_main_menu(bot)

    # register routers in dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # skip updates & start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
