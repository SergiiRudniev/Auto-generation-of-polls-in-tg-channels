import logging

import g4f
from AI import config

class AI:
    def __init__(self, prompt: str = config.prompt) -> None:
        self.prompt = prompt
        self.chat = []
    async def CreateQuiz(self) -> str:
        logging.info("Create Text")
        self.chat.append({"role": "user", "content": self.prompt})
        response = await g4f.ChatCompletion.create_async(model=g4f.models.gpt_4, messages=self.chat)
        self.chat.append({"role": "assistant", "content": response})
        return response