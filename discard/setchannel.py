# cogs/setchannel.py

from discord.ext import commands
from discord.ext.commands import Bot
from core.any import Cog_Extension
import os
import json

class setchannel(Cog_Extension):
    @commands.command()
    async def setchannel(self, ctx, *arg):
        guild_name= ctx.guild.name
        if not os.path.exists(f"settings/{guild_name}.json"):
            with open("settings/origin.json", 'r') as f:
                config = json.load(f)
            json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)
        else: 
            with open(f"settings/{guild_name}.json", 'r') as f:
                config = json.load(f)
        if arg:
            await ctx.message.add_reaction("✅")
            await ctx.send(f"已將歡迎頻道調整至 {arg[0]}!")
            channel_id = int(arg[0][2:-1])
            config["Welcome_channel"] = channel_id
            json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)
            
        else:
            await ctx.message.add_reaction("❌")
            await ctx.send("沒有指定頻道")
            await ctx.send("用法: ~setchannel #頻道名稱")

def setup(bot):
    bot.add_cog(setchannel(bot))