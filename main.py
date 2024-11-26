import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '7656550573:AAFnOlY01aYWpCvjXAiMFn4E2jOzYKZfczE'
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
     await message.answer("Даров")


# dp.message()
# async def echo(message: types.Message):
#     await message.answer("")


dp.message()
async def my_func(message: types.Message):
    if message.text == 'Привет':
        await message.answer("Привет")
    elif message.text == 'Пока':
        await message.anser("Пока")


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
