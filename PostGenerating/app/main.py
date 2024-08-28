import asyncio
import logging
import datetime
import time

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
time.sleep(3)
ai = AI()
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
bot_controller = ControllerBot(bot, CHANNEL_ID)
NON_WORKING_HOURS = list(getenv("NON_WORKING_HOURS").split(","))
async def send_quiz():
    while True:
        try:
            if str(datetime.datetime.now().hour) not in NON_WORKING_HOURS:
                logging.error(str(datetime.datetime.now().hour))
                logging.error(NON_WORKING_HOURS)
                logging.error("Create New Post")
                response = Replace(await ai.CreateQuiz())
                await bot.send_message(CHANNEL_ID, response, parse_mode=ParseMode.MARKDOWN_V2)
            else:
                logging.error("NON_WORKING_HOURS")
        except Exception as e:
            logging.error(f"response: {response}")
            if response == "":
                print("Create New")
                continue
            logging.error(e)
        await asyncio.sleep(int(getenv("DELAY")))
async def main():
    dp.startup.register(send_quiz)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
