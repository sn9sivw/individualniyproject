import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Даров")


# dp.message()
# async def echo(message: types.Message):
#    await message.answer("Йоу")


# @dp.message()
# async def convers(message: types.Message):
#     if message.text == "Бармалей трибубей":
#         await message.answer("Это кто?")

#     else:
#         await message.answer(message.text)


@dp.message()
async def my_func(message: types.Message):
    if message.text == "Привет":
        await message.answer("Приве")
    elif message.text == "Пока":
        await message.answer("Пока")


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
