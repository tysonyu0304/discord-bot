# cogs/rick

from discord.ext import commands
from core.any import Cog_Extension

class rick(Cog_Extension):
    @commands.command()
    async def rick(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=GtL1huin9EE")
    
def setup(bot):
    bot.add_cog(rick(bot))