import logging
import pandas as pd
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

import asyncio

logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)

# ============ !!! Секретный токен !!! ===============
APP_TOKEN = "APP_TOKEN"
# ====================================================

PATH_TO_TODO_TABLE = "todo_result/todo_list.csv"

def get_todo_data():
    return pd.read_csv(PATH_TO_TODO_TABLE)

bot = Bot(token=APP_TOKEN)
dp = Dispatcher()

@dp.message(Command("all"))
async def all_tasks(message: Message):
    await message.answer(
        f"```{get_todo_data().to_markdown()}```",
        parse_mode="Markdown"
    )

@dp.message(Command("add"))
async def add_task(message: Message):
    # В aiogram 3.x нет get_args(), аргументы после команды нужно парсить вручную
    text = message.text.partition(' ')[2].strip()
    if not text:
        await message.reply("Пожалуйста, укажите текст задачи после команды /add")
        return
    new_task = pd.DataFrame({"text": [text], "status": ["active"]})
    updated_tasks = pd.concat([get_todo_data(), new_task], ignore_index=True, axis=0)
    updated_tasks.to_csv(PATH_TO_TODO_TABLE, index=False)
    logging.info(f"Добавил в таблицу задачу - {text}")
    await message.reply(f"Добавил задачу: *{text}*", parse_mode="Markdown")

@dp.message(Command("done"))
async def complete_task(message: Message):
    text = message.text.partition(' ')[2].strip()
    if not text:
        await message.reply("Пожалуйста, укажите текст задачи после команды /done")
        return
    df = get_todo_data()
    df.loc[df.text == text, "status"] = "complete"
    df.to_csv(PATH_TO_TODO_TABLE, index=False)
    logging.info(f"Выполнил задачу - {text}")
    await message.reply(f"Выполнено: *{text}*", parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
