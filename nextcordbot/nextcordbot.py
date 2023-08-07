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
        self.logger = logging.getLogger('nextcord')
        self.logger.setLevel(logging.DEBUG)
        _handler = logging.FileHandler(
            filename=os.path.join(up_dir(__file__), 'logs', f'nextcord{datetime.datetime.now().strftime("%h-%s")}.log'),
            encoding='utf-8',
            mode='w'
        )
        _handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        self.logger.addHandler(_handler)

    def __call__(self):
        self.run(os.getenv("DISCORD_BOT_TOKEN"))

    async def on_ready(self):
        print("On Ready")

    async def on_message(self):
        print("On Message")