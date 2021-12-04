import disnake
from disnake.ext import commands


class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, text):
        await ctx.reply(text)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 1):
        amount = amount + 1
        await ctx.channel.purge(limit=amount)
        return await ctx.send(f"Очищено {amount - 1} сообщений!")
      
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: disnake.User=None, *, reason = "Причина не указана!"):
        if user is not None:
            await ctx.guild.kick(user, reason=reason)
            return await ctx.send(f"Пользоваетль {user.mention} был кикнут по причине **{reason}**")
        else:
            return await ctx.reply("Не указан пользователь!")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: disnake.User=None, *, reason="Причина не указана!"):
        if user is not None:
            await ctx.guild.ban(user, reason=reason)
            return await ctx.send(f"Пользовать {user.mention} был забанен по причине **{reason}**")
        else:
            return await ctx.reply("Не указан пользователь!")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: disnake.User):
        banned_users = await ctx.guild.bans()
        user = disnake.utils.get(banned_users, )


def setup(bot):
    bot.add_cog(Utils(bot))