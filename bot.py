import logging

from aiogram import Bot, Dispatcher, executor, types
from bot_states import UserStates
from aiogram.dispatcher import FSMContext
from bot_database import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)


BOT_TOKEN = "5635786298:AAFwXV33MFsm1dOaNj4TU2NBmwGkvnFObQU"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


async def on_start_my_bot(dp):
    await create_tables()


@dp.message_handler(commands=['start'])
async def start_bot_command(message: types.Message):
    await message.answer("Salom")


@dp.message_handler(commands=['register'])
async def register_bot_command(message: types.Message):
    await message.answer("F.I.O yuboring:")
    await UserStates.fio.set()


@dp.message_handler(state=UserStates.fio, content_types=['text'])
async def get_user_fio_state(message: types.Message, state: FSMContext):
    fio = message.text
    print(fio)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_my_bot)


