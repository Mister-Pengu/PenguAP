import disnake
from disnake.ext import commands


class Events(commands.Cog): 
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if "сало" in message.content.lower():
            await message.reply("смачненьке")


def setup(bot):
    bot.add_cog(Events(bot))
