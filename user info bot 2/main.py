import asyncio
import os
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("token")
ADMIN_ID = int(os.getenv("A_id"))

dp = Dispatcher()

# Random AI-like states
bot_status = [
    "🔍 Scanning user's profile...",
    "🧠 Thinking about how to respond...",
    "💾 Loading encrypted memory blocks...",
    "⚡️ Establishing neural link...",
    "🌐 Syncing with satellite..."
]

# ASCII banner
ascii_banner = """
░█▀█░█░░░█▀▀░█▀▀░█▀▄
░█░█░█░░░█▀▀░█▀▀░█▀▄
░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀
"""

@dp.message(Command("start"))
async def start_handler(message: Message):
    user = message.from_user
    name = user.full_name
    user_id = user.id
    username = user.username or "👤 Not set"

    status_message = random.choice(bot_status)

    reply_text = (
        f"<pre>{ascii_banner}</pre>\n"
        f"🤖 Hello, {name}!\n\n"
        f"{status_message}\n\n"
        f"📎 Profile Summary:\n"
        f"• Name: {name}\n"
        f"• Username: @{username}\n"
        f"• ID: {user_id}\n"
        f"\n"
        f"✅ Connection status: <b>Secure</b>\n"
        f"📡 Bot Core v2.1 initialized.\n"
    )

    await message.answer(reply_text, parse_mode="HTML")

    await message.bot.send_message(
        ADMIN_ID,
        f"🚨 Yangi foydalanuvchi 'Creative Bot'ga ulandi!\n"
        f"👤 {name} | ID: {user_id} | @{username}"
    )


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
