# cogs/ping

from discord.ext import commands
from discord.ext.commands import Bot
from core.any import Cog_Extension

class ping(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"延遲: {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(ping(bot))