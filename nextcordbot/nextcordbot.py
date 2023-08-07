import nextcord
from nextcord.ext import commands



class NextcordBot(commands.Bot):
    
    def __init__(self, *args, **kwargs):
        # You can modify this to accept different intents.
        # Typically, you will want all.
        super().__init__(intents=nextcord.Intents.all(), *args, **kwargs)


    async def on_ready(self):
        print("On Ready")

    async def on_message(self):
        print("On Message")