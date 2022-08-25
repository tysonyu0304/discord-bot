# cogs/setwelcome.py

from discord.ext import commands
from discord.ext.commands import Bot
from core.any import Cog_Extension
import os
import json

class setwelcome(Cog_Extension):
    @commands.command()
    async def setwelcome(self, ctx, *arg):
        guild_name= ctx.guild.name
        if not os.path.exists(f"settings/{guild_name}.json"):
            with open("settings/origin.json", 'r') as f:
                config = json.load(f)
            json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)
        else: 
            with open(f"settings/{guild_name}.json", 'r') as f:
                config = json.load(f)
        if arg:
            if arg[0].upper() == "TRUE":
                config["Welcome_message"] = "True"
                json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)
                await ctx.message.add_reaction("✅")
            elif arg[0].upper() == "FALSE":
                config["Welcome_message"] = "False"
                json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)
                await ctx.message.add_reaction("✅")
            else:
                await ctx.send("錯誤的參數 請輸入True或False")
                await ctx.send("用法: ~setwelcome True或False")
                await ctx.message.add_reaction("❌")
        else:
                await ctx.send("錯誤的參數 請輸入True或False")
                await ctx.send("用法: ~setwelcome True或False")
                await ctx.message.add_reaction("❌")

def setup(bot):
    bot.add_cog(setwelcome(bot))