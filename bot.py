import os

from dotenv import load_dotenv
from twitchio.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=os.getenv("TMI_TOKEN"),
            client_id=os.getenv("CLIENT_ID"),
            nick=os.getenv("BOT_NICK"),
            prefix=os.getenv("BOT_PREFIX"),
            initial_channels=[i.strip() for i in os.getenv("CHANNELS").split(",")],
        )

    async def event_ready(self):
        "Called once when the bot goes online."
        print(f"{os.environ['BOT_NICK']} is online")
        ws = bot._ws  # this is only needed to send messages within event_ready
        # await ws.send_privmsg(os.getenv('CHANNEL'), f"/me is looking for food")

    async def event_message(self, ctx):
        "Runs every time a message is sent in chat."
        # make sure the bot ignores itself and the streamer
        if ctx.author.name.lower() == os.getenv("BOT_NICK").lower():
            return
        await self.handle_commands(ctx)

    # Commands use a different decorator
    @commands.command(name="test")
    async def my_command(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")


if __name__ == "__main__":
    load_dotenv()

    channelz = [i.strip() for i in os.getenv("CHANNELS").split(",")]
    print(f"Connecting to {channelz}")
    bot = Bot()
    bot.run()
