# cogs/time/py

import discord
from discord.ext import commands
from core.any import Cog_Extension
from datetime import datetime

class time(Cog_Extension):
    @commands.command()
    async def time(self, ctx):
        now = datetime.now()
        await ctx.send(now.strftime("%Y-%m-%d %H:%M:%S"))

    @commands.command()
    async def timer(ctx, *arg):
        if not arg:
            await ctx.send("請輸入時間")
        else:
            try:
                int(arg[0])
            except ValueError:
                await ctx.send("請輸入數字")
            if int(arg[0]) > 86400:
                await ctx.send("不能超過一天")
            elif int(arg[0]) < 0:
                await ctx.send("不能小於0秒")
            else:
                await ctx.send("Timer: " + str(arg[0]) + "秒")
                second = int(arg[0])
                while second > 0:
                    second -= 1
                    if second <= 0:
                        await ctx.send("完成")
                        break

def setup(bot):
    bot.add_cog(time(bot))