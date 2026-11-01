import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ChatMemberStatus, ChatType
from transformers import pipeline

classifier = pipeline("text-classification", model="sismetanin/rubert-toxic-pikabu-2ch")


def check_toxicity(text: str):
    result = classifier(text)[0]
    print(f"Текст: '{text}' | Ответ модели: {result}")          #мониторинг логов ИИ в консоли
    label = result['label']
    score = result['score']
    if label in ['LABEL_1'] and score >= 0.81:
        return True
    return False


load_dotenv()
token = os.getenv("BOT_TOKEN")                                  #передача токена в программу

if not token:
    raise ValueError("Неправильный токен / Incorrect token")

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Привет! Я буду фильтровать комментарии в твоём канале!')


@dp.message(F.text, F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def check_message(message: Message):
    if message.sender_chat:
        return

    # Получаем текст и сразу проверяем, что он не пустой
    user_text = message.text
    if not user_text:
        return

    member = await bot.get_chat_member(message.chat.id, message.from_user.id)

    if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
        return

    is_bad = check_toxicity(user_text)

    if is_bad:
        try:
            await message.delete()
            user_mention = message.from_user.mention_html()
            warning_msg = await message.answer(
                f"⚠️ {user_mention}, ваше сообщение было удалено из-за подозрения на токсичность.",
                parse_mode="HTML"
            )
            print(f"Удалён токсичный комментарий от {message.from_user.full_name}: {user_text}")

            await asyncio.sleep(7)
            await warning_msg.delete()
        except Exception as e:
            print(f"Не удалось обработать сообщение: {e}")


async def main():
  logging.basicConfig(level=logging.INFO)
  print("Бот запущен.")
  await dp.start_polling(bot)


if __name__ == '__main__':
  asyncio.run(main())
