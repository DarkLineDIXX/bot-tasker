from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ACCESS_DATA = {
    "Сотрудник1": {"login": "user1", "password": "pass1"},
    "Сотрудник2": {"login": "user2", "password": "pass2"},
}

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["Access"])
async def send_access(message: types.Message):
    name = message.from_user.first_name
    if name in ACCESS_DATA:
        data = ACCESS_DATA[name]
        await message.answer(f"🔐 Логин: `{data['login']}`\n🔑 Пароль: `{data['password']}`", parse_mode="Markdown")
    else:
        await message.answer("🚫 У вас нет доступа к данным кассы.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
