class Bot:
    def __init__(self, bot, CHANNEL_ID):
        self.__bot = bot
        self.__CHANNEL_ID = CHANNEL_ID

    async def send_quiz(self, question: str, options: list, correct_option_id: int) -> None:
        await self.__bot.send_poll(
            chat_id=self.__CHANNEL_ID,
            question=question,
            options=options,
            is_anonymous=True,
            type="quiz",
            correct_option_id=correct_option_id
        )
