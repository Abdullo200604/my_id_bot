import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = 'bot token'
ADMIN_ID = 123456789  # <-- BU YERGA ADMIN TELEGRAM ID sini yozing

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user = message.from_user
    full_name = user.full_name
    user_id = user.id
    username = user.username or 'yo‘q'

    # Terminalga chiqarish
    print(f"Botga /start yuborgan foydalanuvchi:\n"
          f"Ism: {full_name}\n"
          f"Username: @{username}\n"
          f"ID: {user_id}")

    # Foydalanuvchiga o'ziga xabar yuborish
    await message.answer(
        f"Salom {full_name}!\n"
        f"Sizning ma'lumotlaringiz:\n"
        f"Ism: {full_name}\n"
        f"Username: @{username}\n"
        f"ID: {user_id}"
    )

    # Admin ga xabar yuborish
    await message.bot.send_message(
        ADMIN_ID,
        f"Yangi foydalanuvchi botga start bosdi!\n"
        f"Ism: {full_name}\n"
        f"Username: @{username}\n"
        f"ID: {user_id}"
    )


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
