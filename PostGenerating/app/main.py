import asyncio
import logging

from aiogram import Bot, Dispatcher
from os import getenv
from BotController.Bot import Bot as ControllerBot
from AI.Ai import AI
from dotenv import load_dotenv
from aiogram.enums import ParseMode
from Replacer.Replacer import Replace
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
API_TOKEN = getenv("TOKEN")
CHANNEL_ID = getenv("CHANNEL_ID")

ai = AI()
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
bot_controller = ControllerBot(bot, CHANNEL_ID)
async def send_quiz():
    while True:
        try:
            logging.info("Create New Quiz")
            response = Replace(await ai.CreateQuiz())
            await bot.send_message(CHANNEL_ID, response, parse_mode=ParseMode.MARKDOWN_V2)
        except Exception as e:
            logging.error(f"response: {response}")
            if not response:
                continue
            logging.error(e)
        await asyncio.sleep(int(getenv("DELAY")))
async def main():
    dp.startup.register(send_quiz)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
