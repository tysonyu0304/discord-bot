# cogs/setadmins.py
# 先擱置

from discord.ext import commands
from core.any import Cog_Extension
import os
import json

class setadmins(Cog_Extension):
    @commands.command()
    @commands.is_owner()
    async def setadmins(self, ctx, *arg):
        guild_name = ctx.guild.name
        if not os.path.exists(f"settings/{guild_name}.json"):
            with open("settings/origin.json", 'r') as f:
                config = json.load(f)
            json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)
        else: 
            with open(f"settings/{guild_name}.json", 'r') as f:
                config = json.load(f)
        if arg:
            config["admins"].append(arg[0][2:-1])
            json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)
            await ctx.message.add_reaction("✅")
            await ctx.send(f"已將 {arg[0][2:-1]} 設為管理員")
        else:
            await ctx.send("沒有指定管理員 請在指令後面直接@管理員")
            await ctx.message.add_reaction("❌")

def setup(bot):
    bot.add_cog(setadmins(bot))