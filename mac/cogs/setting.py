# cogs/setting.py

from discord.ext import commands
from discord.ext.commands import Bot
from core.any import Cog_Extension

class setting(Cog_Extension):
    @commands.command()
    async def setting(self, ctx):
        with open("setting.txt", 'r', encoding="utf-8") as f:
            setting_text = f.read()
        await ctx.send(setting_text)

def setup(bot):
    bot.add_cog(setting(bot))
