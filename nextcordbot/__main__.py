from nextcordbot import NextcordBot
import nextcord

def main():
    # Defaults when running the bot through `py -m nextcordbot`

    bot = NextcordBot(

            intents=nextcord.Intents.all(),

            status=nextcord.Status.online,

            activity=nextcord.Activity(
                name="with Nextcord",
                type=nextcord.ActivityType.playing,
            ),
        )
    
    bot()

if __name__ == "__main__":
    main()
