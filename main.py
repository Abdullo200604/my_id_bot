import asyncio
import os
import random
import json
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

# .env faylidan tokenlarni olish
TOKEN_1 = os.getenv("token1")  # 1-bot uchun token
TOKEN_2 = os.getenv("Token")  # 2-bot uchun token
ADMIN_ID = int(os.getenv("A_id"))  # Admin ID

# Dispatcherlar
dp_1 = Dispatcher()
dp_2 = Dispatcher()

# Statistika (doimiy saqlash uchun fayl)
STAT_FILE = "user_stats.json"

# Statistikani yuklash
def load_stats():
    if os.path.exists(STAT_FILE):
        with open(STAT_FILE, "r") as f:
            data = json.load(f)
            return set(data.get("bot1_users", [])), set(data.get("bot2_users", []))
    return set(), set()

# Statistikani saqlash
def save_stats():
    with open(STAT_FILE, "w") as f:
        json.dump({
            "bot1_users": list(bot_1_users),
            "bot2_users": list(bot_2_users)
        }, f)

# Foydalanuvchilar to‘plami
bot_1_users, bot_2_users = load_stats()

# Random statuslar
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

# 1-bot start handler
@dp_1.message(Command("start"))
async def start_handler(message: Message):
    user = message.from_user
    name = user.full_name
    user_id = user.id
    username = user.username or "👤 Not set"

    # Statistika uchun
    bot_1_users.add(user_id)
    save_stats()

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


# 2-bot start handler
@dp_2.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user = message.from_user
    full_name = user.full_name
    user_id = user.id
    username = user.username or "👤 Not set"

    # Statistika uchun
    bot_2_users.add(user_id)
    save_stats()

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


# 1-bot statistika komandasi
@dp_1.message(Command("stats"))
async def stats_handler_1(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Bu buyruq faqat admin uchun.")
    
    await message.answer(
        f"📊 <b>Bot statistikasi:</b>\n"
        f"• 👥 Foydalanuvchilar soni: {len(bot_1_users)}",
        parse_mode="HTML"
    )


# 2-bot statistika komandasi
@dp_2.message(Command("stats"))
async def stats_handler_2(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Bu buyruq faqat admin uchun.")
    
    await message.answer(
        f"📊 <b>Bot statistikasi:</b>\n"
        f"• 👥 Foydalanuvchilar soni: {len(bot_2_users)}",
        parse_mode="HTML"
    )


# Asosiy funksiya
async def main() -> None:
    bot_1 = Bot(token=TOKEN_1)
    bot_2 = Bot(token=TOKEN_2)

    task_1 = asyncio.create_task(dp_1.start_polling(bot_1))
    task_2 = asyncio.create_task(dp_2.start_polling(bot_2))

    await asyncio.gather(task_1, task_2)


if __name__ == "__main__":
    asyncio.run(main())
