#cogs/hi.py

from discord.ext import commands
from core.any import Cog_Extension

class hi(Cog_Extension):
    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f"Hi!!! <@{ctx.author.id}>")
        
def setup(bot):
    bot.add_cog(hi(bot))