# cogs/settings.py

import discord
from discord.ext import commands
from core.any import Cog_Extension
import json
import os

class settings(Cog_Extension):
    @commands.command()
    async def settings(self, ctx):
        embed=discord.Embed(title="機器人設定", description="查看各項設定的指令", color=0xd00101)
        embed.add_field(name="-setwelcome", value="調整是否要傳送歡迎訊息", inline=False)
        embed.add_field(name="-setchannel", value="調整歡迎訊息的頻道", inline=False)
        embed.add_field(name="-ping", value="查看機器人的延遲", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def setwelcome(self, ctx, *arg):
        guild_name= ctx.guild.name
        if not os.path.exists(f"Configs/{guild_name}.json"):
            with open("Configs/sample.json", 'r') as f:
                config = json.load(f)
            json.dump(config, open(f"Configs/{guild_name}.json", 'w'), indent = 4)
        else: 
            with open(f"Configs/{guild_name}.json", 'r') as f:
                config = json.load(f)
        if arg:
            if arg[0].upper() == "TRUE":
                config["settings"]["Welcome_message"] = "True"
                json.dump(config, open(f"Configs/{guild_name}.json", 'w'), indent = 4)
                await ctx.message.add_reaction("✅")
            elif arg[0].upper() == "FALSE":
                config["settings"]["Welcome_message"] = "False"
                json.dump(config, open(f"Configs/{guild_name}.json", 'w'), indent = 4)
                await ctx.message.add_reaction("✅")
            else:
                await ctx.send("錯誤的參數 請輸入True或False")
                await ctx.send("用法: ~setwelcome True或False")
                await ctx.message.add_reaction("❌")
        else:
                await ctx.send("錯誤的參數 請輸入True或False")
                await ctx.send("用法: ~setwelcome True或False")
                await ctx.message.add_reaction("❌")

    @commands.command()
    async def setchannel(self, ctx, *arg):
        guild_name= ctx.guild.name
        if not os.path.exists(f"Configs/{guild_name}.json"):
            with open("Configs/sample.json", 'r') as f:
                config = json.load(f)
            json.dump(config, open(f"Configs/{guild_name}.json", 'w'), indent = 4)
        else: 
            with open(f"Configs/{guild_name}.json", 'r') as f:
                config = json.load(f)
        if arg:
            await ctx.message.add_reaction("✅")
            await ctx.send(f"已將歡迎頻道調整至 {arg[0]}!")
            channel_id = int(arg[0][2:-1])
            config["settings"]["Welcome_channel"] = channel_id
            json.dump(config, open(f"Configs/{guild_name}.json", 'w'), indent = 4)

        else:
            await ctx.message.add_reaction("❌")
            await ctx.send("沒有指定頻道")
            await ctx.send("用法: ~setchannel #頻道名稱")

    @commands.command()
    async def setchannel2(self, ctx, *arg):
        guild_name = ctx.guild.name
        if not os.path.exists(f"Configs/{guild_name}.json"):
            with open("Configs/sample.json", 'r') as f:
                config = json.load(f)
            json.dump(config, open(f"Configs/{guild_name}.json", 'w'), indent = 4)
        else:
            with open("Configs/sample.json", 'r') as f:
                config = json.load(f)
        if arg:
            await ctx.message.add_reaction("✅")
            await ctx.send(f"已將指令訊息頻道調整至 {arg[0]}!")
            channel_id = int(arg[0][2:-1])
            config["settings"]["Commands_channel"] = channel_id
            json.dump(config, open(f"Configs/{guild_name}.json", 'w'), indent = 4)

def setup(bot):
    bot.add_cog(settings(bot))
