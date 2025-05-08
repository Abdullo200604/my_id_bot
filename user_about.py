import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8159987403:AAGrLtMU1jZ9y_qkU3Cv39D832o2e1DYim4'
ADMIN_ID = 7346730386  # <-- BU YERGA ADMIN TELEGRAM ID sini yozing

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user = message.from_user
    full_name = user.full_name
    user_id = user.id
    username = user.username or 'yo‘q'

    print(f"Botga /start yuborgan foydalanuvchi:\n"
          f"Ism: {full_name}\n"
          f"Username: @{username}\n"
          f"ID: {user_id}")

    await message.answer(
        f"📘 ════ USER INFORMATION ════ 📘\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🆔 Identification\n"
        f"• 🧑 Username: @{username}\n"
        f"• 🔖 ID: {user_id}\n"
        f"• 👤 Name: {full_name}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🌐 Account Details\n"
        f"• 🌍 Language: en\n"
        f"• 🛰️ Data Center: 2\n"
        f"• 🎖️ Account Type: 🌟 Premium 👤 User\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📅 Last Checked\n"
        f"• 📅 Date: 2025-05-08 06:47:37 UTC"
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"Yangi foydalanuvchi botga start bosdi!\n"
        f"Ism: {full_name}\n"
        f"Username: @{username}\n"
        f"ID: {user_id}"
    )


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
