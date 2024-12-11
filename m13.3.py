from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот для общения.Задай любой вопрос и я на него отвечу в течение 10 секунд!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)