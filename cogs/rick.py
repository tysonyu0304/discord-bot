# cogs/rick.py

import discord
from discord.ext import commands
from core.any import Cog_Extension
import random

class rick(Cog_Extension):
    @commands.command(pass_context=True)
    async def rick(self, ctx, *arg):
        if not arg:
            embed=discord.Embed(title="-rick", description="顯示此清單")
            embed.add_field(name="-rick gif", value="出現 rick astley 的 gif", inline=False)
            embed.add_field(name="-rick old", value="出現 never gonna give you up 的舊版網址", inline=False)
            embed.add_field(name="-rick new", value="出現 never gonna give you up 的新版網址", inline=False)
            await ctx.send(embed=embed)
        elif arg[0].upper() == "GIF":
            await ctx.send(file=discord.File("rick.gif"))
        elif arg[0].upper() == "OLD":
            await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        elif arg[0].upper() == "NEW":
            await ctx.send("https://www.youtube.com/watch?v=GtL1huin9EE")

def setup(bot):
    bot.add_cog(rick(bot))