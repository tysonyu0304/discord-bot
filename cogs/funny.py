# cogs/funny.py

import discord
from discord.ext import commands
from core.any import Cog_Extension

class funny(Cog_Extension):
    @commands.command()
    async def funny(self, ctx):
        embed=discord.Embed(title="-funny", description="顯示此清單", color=0xfff700)
        embed.add_field(name="-hi", value="我會跟你問好", inline=False)
        embed.add_field(name="-rick", value="登~登~登~登登", inline=False)
        embed.add_field(name="-todolist", value="查看作者的todo list", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(funny(bot))
