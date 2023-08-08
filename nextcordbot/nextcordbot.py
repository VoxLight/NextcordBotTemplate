import os
import datetime
from .utils import up_dir
import logging

import nextcord
from nextcord.ext import commands



class NextcordBot(commands.Bot):
    
    def __init__(self, *args, **kwargs):
        # API referance for the commands.Bot object, which we inherit:
        # https://docs.nextcord.dev/en/stable/ext/commands/api.html#bot
        super().__init__(*args, **kwargs)

        # Help with the logger: 
        # https://docs.nextcord.dev/en/stable/logging.html
        # Set up logging handler for nextcord logs
        nextcord_logs = logging.getLogger('nextcord')
        nextcord_logs.setLevel(logging.DEBUG)
        _handler = logging.FileHandler(
            filename=os.path.join(up_dir(__file__), 'logs', 'nextcord.log'),
            encoding='utf-8',
            mode='w'
        )
        nextcord_logs.addHandler(_handler)

        # Set up the internal logger
        self.log = logging.getLogger('bot')
        self.log.setLevel(logging.DEBUG)
        _handler = logging.FileHandler(
            filename=os.path.join(up_dir(__file__), 'logs', f'bot {datetime.datetime.now().strftime("%h-%s")}.log'),
            encoding='utf-8',
            mode='w'
        )
        _handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        self.log.addHandler(_handler)

    def __call__(self):
        self.run(os.getenv("DISCORD_BOT_TOKEN"))

    async def on_ready(self):
        self.log.info("On Ready!")

    async def on_message(self, message: nextcord.Message):
        print("Message Sent:", message.created_at, message.content)