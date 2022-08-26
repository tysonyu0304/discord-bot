from discord.ext import commands
from datetime import datetime
import json
import os
import discord

# 載入 config.json
with open("config.json", 'r') as f:
    config = json.load(f)

# 設定 intents
intents = discord.Intents.all()
intents.members = True
# intents.typing = True

# 建立 bot
bot = commands.Bot(command_prefix=config['command_prefix'], owner_id = config["owner_id"], intents = intents)
bot.remove_command('help')

# 設定 bot
token = os.getenv('DISCORD_BOT_TOKEN')

# 載入 cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        # print(filename[:-3])
        bot.load_extension(f'cogs.{filename[:-3]}')

# 當機器人啟動時觸發的事件
@bot.event
async def on_ready():
    print("bot is ready, now logging as {}".format(bot.user.name))
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = "~help"))

# 當機器人加入到新的伺服器時觸發的事件
@bot.event
async def on_guild_join(guild):
    await guild.system_channel.send(f"歡迎使用 {bot.user.name}")
    await guild.system_channel.send("請先使用 ~setting 查看設定事項")
    guild_name = guild.name
    if not os.path.exists(f"settings/{guild_name}.json"):
        with open("settings/origin.json", 'r') as f:
            config = json.load(f)
        json.dump(config, open(f"settings/{guild_name}.json", 'w'), indent = 4)

# 當伺服器有人加入時觸發的事件
@bot.event
async def on_member_join(member):
    with open(f"settings/{member.guild.name}.json", 'r') as f:
        config = json.load(f)
    if config["Welcome_message"] == "True":
        await bot.get_channel(config["Welcome_channel"]).send(f"<@{member.id}> 歡迎加入 {member.guild.name}")

# 當伺服器有人離開時觸發的事件
@bot.event
async def on_member_remove(member):
    with open(f"settings/{member.guild.name}.json", 'r') as f:
        config = json.load(f)
    if config["Welcome_message"] == "True" and member.id != bot.user.id:
        await bot.get_channel(config["Welcome_channel"]).send(f"喔不 `{member.name}` 離開了我們")

# 當指令報錯時觸發的事件
@bot.event
async def on_commands_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("你沒有權限")

# 發送 help 列表
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="-help", description="會顯示這個清單", color=0x00ff4c)
    embed.add_field(name="-settings", value="查看如何調整各項機器人設定", inline=True)
    embed.add_field(name="-funny", value="查看一些好玩的指令", inline=False)
    embed.add_field(name="-bank", value="查看如何使用銀行系統", inline=True)
    embed.set_thumbnail(url = bot.user.avatar_url)
    await ctx.send(embed=embed)

bot.run(token)