# cogs/bank.py

from asyncio import tasks
import discord
from discord.ext import commands
from core.any import Cog_Extension
import json
import os
import random

class bank(Cog_Extension):
    @commands.command()
    # 銀行系統
    async def bank(self, ctx, *arg):
        if not os.path.exists(f"Configs/{ctx.guild.name}.json"):
            with open("Configs/sample.json", 'r') as f:
                config = json.load(f)
            json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
        with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
            config = json.load(f)
        '''
        if not os.path.exists(f"bank/{ctx.guild.name}.json"): # 如果沒有這個伺服器的資料
            json.dump([], open(f"bank/{ctx.guild.name}.json", 'w'), indent = 4)
        with open(f"bank/{ctx.guild.name}.json", 'r') as f:
            config = dict(json.load(f))
        '''

        if not f"{ctx.author.id}" in config["bank"]: # 如果沒有這個人的資料
            config["bank"][f"{ctx.author.id}"] = 1000
            embed=discord.Embed(title="成功開戶", description= f"已經幫 {ctx.author.name} 建立戶頭, 並提供1000元開戶金!!!", color=0x00ffcc)
            await ctx.send(embed=embed)
        json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
        
        if not arg: # 如果沒有參數
            embed=discord.Embed(title="沒有輸入操作指令", description="用法 : -bank <指令> <參數> 或 輸入 -bank help 以獲得更多說明", color=0x00ffcc)
            await ctx.send(embed=embed)

        elif arg[0].upper() == "CHECK": # 查看餘額
            if len(arg) == 1: # 如果只有一個參數
                embed=discord.Embed(title="{}的".format(ctx.bot.get_user(ctx.author.id))) 
                embed.add_field(name="帳戶餘額", value="{} 元".format(config["bank"][f"{ctx.author.id}"]), inline=False)
                embed.set_thumbnail(url = ctx.author.avatar_url)
                await ctx.send(embed=embed)
            elif arg[1][2:-1] in config: # 如果帳號id存在
                id = int(arg[1][2:-1])
                name = ctx.bot.get_user(id)
                embed=discord.Embed(title="{}的".format(name))
                embed.add_field(name="帳戶餘額", value="{} 元".format(config["bank"][f"{arg[1][2:-1]}"]), inline=False)
                embed.set_thumbnail(url = name.avatar_url)
                await ctx.send(embed=embed)
            else:
                try:
                    await commands.MemberConverter().convert(ctx, arg[1]) # 如果帳號名字可以轉換成id
                except:
                    embed=discord.Embed(title="沒有這個人的帳戶", description="請確認輸入的帳戶id是否正確", color=0x00ffcc)
                    await ctx.send(embed=embed)
                else:
                    target = await commands.MemberConverter().convert(ctx, arg[1])
                    if target in config["bank"]: # 如果帳號id存在
                        embed=discord.Embed(title="{}的".format(target.name))
                        embed.add_field(name="帳戶餘額", value="{} 元".format(config["bank"][f"{target.id}"]), inline=False)
                        embed.set_thumbnail(url = target.avatar_url)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(title="沒有這個人的帳戶", description="請確認輸入的帳戶id是否正確", color=0x00ffcc)
                        await ctx.send(embed=embed)

        elif arg[0].upper() == "ROB":
            can = await check_data(ctx, ctx.author.id)
            if can:
                if len(arg) == 1: # 如果只有一個參數
                    await ctx.send("你沒有指定目標 我不知道你要搶誰的錢")
                elif arg[1].upper() == "CHECK":
                    # await ctx.send("!!")
                    with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
                        config = dict(json.load(f))
                        if str(ctx.author.id) in config["rob_times"]:
                            await ctx.send("你還可以搶 {} 次".format(config["rob_times"][f"{ctx.author.id}"]))
                elif arg[1][2:-1] in config["bank"]: # 如果帳號id存在
                    if not arg[1][2:-1] == str(ctx.author.id):
                        target_id = arg[1][2:-1]
                        random_int = random.randint(0, config["bank"][target_id]) # 產生一個不超過對象餘額的隨機數
                        if random_int == 0: # 如果隨機數為0
                            await ctx.send("你有夠爛 一毛都搶不到")
                        elif random_int == config[target_id]: # 如果隨機數等於對象餘額
                            name = ctx.bot.get_user(int(target_id))
                            await ctx.send("你有夠狠 把 {} 的 {} 元全搶過來了".format(name, config["bank"][target_id]))
                        else:
                            await ctx.send("你搶到了 {} 元".format(random_int))
                        config["bank"][f"{ctx.author.id}"] += random_int
                        config["bank"][target_id] -= random_int
                        json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                        await write_data(ctx, ctx.author.id)
                    else:
                        await ctx.send("你不能搶自己的錢")
                else:
                    try:
                        await commands.MemberConverter().convert(ctx, arg[1])
                    except:
                        await ctx.send("沒有這個人的資料")
                    else:
                        member = await commands.MemberConverter().convert(ctx, arg[1])
                        if member.id in config["bank"]:
                            if not member.id == ctx.author.id:
                                if str(member.id) in config["bank"]:
                                    random_int = random.randint(0, config["bank"][f"{member.id}"]) # 產生一個不超過對象餘額的隨機數
                                    target_id = str(member.id)
                                    if random_int == 0: # 如果隨機數為0
                                        await ctx.send("你有夠爛 一毛都搶不到")
                                    elif random_int == config["bank"][target_id]: # 如果隨機數等於對象餘額
                                        name = ctx.bot.get_user(int(target_id))
                                        await ctx.send("你有夠狠 把 {} 的 {} 元全搶過來了".format(name, config["bank"][target_id]))
                                    else:
                                        await ctx.send("你搶到了 {} 元".format(random_int))
                                    config["bank"][f"{ctx.author.id}"] += random_int
                                    config["bank"][target_id] -= random_int
                                    json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                                    await write_data(ctx, ctx.author.id)
                            else:
                                await ctx.send("你不能搶自己的錢")
                        else:
                            await ctx.send("沒有這個人的資料")
            else:
                await ctx.send("你今天的搶劫次數已經用完了 明天再來吧!")

        elif arg[0].upper() == "TRANSFER":
            with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
                set = json.load(f)
            if len(arg) == 1:
                await ctx.send("沒有指定用戶 /n用法: ~bank transfer <@用戶> <金額>")
            elif arg[1][2:-1] in set["bank"]:
                target_id = arg[1][2:-1]
                if len(arg) == 2 :
                    await ctx.send("沒有指定金額 /n用法: ~bank transfer <@用戶> <金額>")
                elif arg[1][2:-1] == ctx.author.id:
                    await ctx.send("不能轉帳給自己 /n用法: ~bank transfer <@用戶> <金額>")
                else:
                    try:
                        int(arg[2])
                    except:
                        if arg[2].upper() == "ALL":
                            all = set["bank"][f"{ctx.author.id}"]
                            set["bank"][f"{ctx.author.id}"] -= all
                            set["bank"][target_id] += all
                            json.dump(set, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                            await ctx.send("已將您的所有餘額轉帳給 {}".format(ctx.bot.get_user(int(target_id))))
                        else: 
                            await ctx.send("金額輸入錯誤 請輸入整數")
                    else:
                        if int(arg[2]) > set["bank"][f"{ctx.author.id}"]:
                            await ctx.send("你的餘額不足 請輸入小於等於你的餘額 (您目前有 {} 元) /n用法: ~bank transfer <@用戶> <金額>".format(set["bank"][f"{ctx.author.id}"]))
                        else:
                            set["bank"][f"{ctx.author.id}"] -= int(arg[2])
                            set["bank"][target_id] += int(arg[2])
                            json.dump(set, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                            await ctx.message.add_reaction("✅")
                            await ctx.send(f"已經成功轉帳給 {ctx.bot.get_user(int(target_id))} {arg[2]} 元")
            else:
                try:
                    await commands.MemberConverter().convert(ctx, arg[1])
                except:
                    await ctx.send("沒有這個用戶 請確認他是否已經開戶 \n用法: ~bank transfer <@用戶> <金額>")
                else:
                    member = await commands.MemberConverter().convert(ctx, arg[1])
                    id = str(member.id)
                    if len(arg) == 2:
                        await ctx.send("沒有指定金額 \n用法: ~bank transfer <@用戶> <金額>")
                    elif id == ctx.author.id:
                        await ctx.send("不能轉帳給自己 \n用法: ~bank transfer <@用戶> <金額>")
                    else:
                        try:
                            int(arg[2])
                        except:
                            if arg[2].upper() == "ALL":
                                all = set["bank"][f"{ctx.author.id}"]
                                set["bank"][f"{ctx.author.id}"] -= all
                                set["bank"][str(id)] += all
                                json.dump(set, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                                await ctx.send("已將您的所有餘額 {} 元轉帳給 {}".format(all, member))
                            else: 
                                await ctx.send("金額輸入錯誤 請輸入整數")
                        else:
                            if int(arg[2]) > set["bank"][f"{ctx.author.id}"]:
                                await ctx.send("你的餘額不足 請輸入小於等於你的餘額 (您目前有 {} 元) \n用法: ~bank transfer <@用戶> <金額>".format(set["bank"][f"{ctx.author.id}"]))
                            else:
                                set["bank"][f"{ctx.author.id}"] -= int(arg[2])
                                set["bank"][id] += int(arg[2])
                                json.dump(set, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                                await ctx.message.add_reaction("✅")
                                await ctx.send(f"已經成功轉帳給 {member} {arg[2]} 元")

        elif arg[0].upper() == "HELP":
            with open("bank_help.txt", 'r', encoding="utf-8") as f:
                help_text = f.read()
            await ctx.send(help_text)
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def bgive(self, ctx, *arg):
        with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
            config = json.load(f)
        if not arg:
            await ctx.send("沒有指定用戶 \n用法: ~bgive <@用戶> <金額>")
        elif arg[0][2:-1] in config["bank"]:
            if not len(arg) == 1:
                try:
                    config["bank"][f"{arg[0][2:-1]}"] += int(arg[1])
                    json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                    await ctx.message.add_reaction("✅")
                except:
                    await ctx.send("金額輸入錯誤 請輸入整數")
            else:
                await ctx.send("沒有指定金額")
                await ctx.send("用法: ~bgive <@用戶> <金額>")
        else:
            if not len(arg) == 1:
                try:
                    await commands.MemberConverter().convert(ctx, arg[0])
                except:
                    await ctx.send("沒有這個用戶 請確認他是否已經開戶")
                    await ctx.send("用法: ~bgive <@用戶> <金額>")
                else:
                    try:
                        member = await commands.MemberConverter().convert(ctx, arg[0])
                        config["bank"][f"{member.id}"] += int(arg[1])
                        json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                        await ctx.message.add_reaction("✅")
                    except:
                        await ctx.send("金額輸入錯誤 請輸入整數")
            else:
                await ctx.send("沒有指定金額")
                await ctx.send("用法: ~bgive <@用戶> <金額>")
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def bset(self, ctx, *arg):
        with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
            config = json.load(f)
        if not arg:
            await ctx.send("沒有指定用戶")
            await ctx.send("用法: ~bset <@用戶> <金額>")
        elif arg[0][2:-1] in config["bank"]:
            if not len(arg) == 1:
                try:
                    config["bank"][f"{arg[0][2:-1]}"] = int(arg[1])
                    json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
                    await ctx.message.add_reaction("✅")
                except:
                    await ctx.send("金額輸入錯誤 請輸入整數")
            else:
                await ctx.send("沒有指定金額")
                await ctx.send("用法: ~bset <@用戶> <金額>")
        else:     
            await ctx.send("沒有這個用戶 請確認他是否已經開戶")
            await ctx.send("用法: ~bset <@用戶> <金額>")
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def breset(self, ctx, *arg):
        if not arg:
            await ctx.send("沒有輸入指令")
        elif arg[0].upper() == "MONEY":
            with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
                set = json.load(f)
            for i in set:
                set["bank"][i] = 1000
            json.dump(set, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
            await ctx.send("金額已經重置")
        elif arg[0].upper() == "ROB":
            with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
                config = json.load(f)
            for i in config:
                config["rob_times"][i] = 1
            config["rob_times"]["521308593136467979"] = 100000000
            json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
            await ctx.send("次數已經重置")

    @tasks.loop(hour = 24)
    async def rob_reset(self, ctx):
        with open(f"Configs/{ctx.guild.name}.json", 'r') as f:
            config = json.load(f)
        for i in config:
            config["rob_times"][i] = 1
        config["rob_times"]["521308593136467979"] = 100000000
        json.dump(config, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
    
async def read_data(ctx):
    if not os.path.exists(f"Configs/{ctx.guild.name}.json"):
        with open(f"Configs/sample.json", 'w') as f:
            config = json.load(f)
        with open(f"Configs/{ctx.guild.name}.json", 'w') as f:
            json.dump(config, f, indent = 4)
    with open(f"Configs/{ctx.guild.name}.json", "r") as f:
        users = json.load(f)
    return users

async def check_data(ctx, user):
    users = await read_data(ctx)
    if not str(user) in users["rob_times"]:
        users["rob_times"][str(user)] = 1
        json.dump(users, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)
        return True
    elif str(user) in users["rob_times"] and users["rob_times"][f"{user}"] > 0:
        return True
    else:
        return False

async def write_data(ctx, user):
    with open(f"Configs/{ctx.guild.name}.json", "r") as f:
        users = json.load(f)
    users["rob_times"][f"{user}"] -= 1
    json.dump(users, open(f"Configs/{ctx.guild.name}.json", 'w'), indent = 4)

def setup(bot):
    bot.add_cog(bank(bot))