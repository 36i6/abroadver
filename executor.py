from environs import Env
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook

env = Env()
env.read_env(".env")
TELEGRAM_API_TOKEN = env.str("TELEGRAM_API_TOKEN")

WEBHOOK_HOST = 'https://*****'
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = 7771

bot = Bot(TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    await bot.delete_webhook()
