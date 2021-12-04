import os

import disnake
import jishaku
from disnake.ext import commands

from keep_alive import keep_elive


bot = commands.Bot(command_prefix="$", Intents=disnake.Intents.all())

jishaku.Flags.NO_UNDERSCORE = True
jishaku.Flags.NO_DM_TRACEBACK = True

cogs = ["cogs.events", "cogs.commands", "jishaku"]


@bot.event
async def on_ready():
    for cog in cogs:
        bot.load_extension(cog)

    print("BOT_CONNECTED")

keep_elive()
bot.run(os.environ["TOKEN"])