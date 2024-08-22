import asyncio
import logging

from aiogram import Bot, Dispatcher
from os import getenv
from BotController.Bot import Bot as ControllerBot
from AI.Ai import AI
from Parser.ParserQuiz import Parse
from dotenv import load_dotenv

load_dotenv()
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
            response = await ai.CreateQuiz()
            question, options, correct_option_id = Parse(response)
            await bot_controller.send_quiz(question, options, correct_option_id)
        except Exception as e:
            logging.error(f"response: {response}")
            logging.error(e)
        await asyncio.sleep(30)
async def main():
    dp.startup.register(send_quiz)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
