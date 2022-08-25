# cogs/bgive.py
'''
from discord.ext import commands
from core.any import Cog_Extension
import json

class bgive(Cog_Extension):
    @commands.command()
    async def bgive(self, ctx, *arg):
        with open(f"settings/{ctx.guild.name}.json", 'r') as f:
            set = json.load(f)
        admin_id = set["admins"]
        if str(ctx.author.id) in admin_id:
            with open(f"bank/{ctx.guild.name}.json", 'r') as f:
                config = json.load(f)
            if not arg:
                await ctx.send("沒有指定用戶")
                await ctx.send("用法: ~bgive <@用戶> <金額>")
            elif arg[0][2:-1] in config:
                if not len(arg) == 1:
                    try:
                        config[f"{arg[0][2:-1]}"] += int(arg[1])
                        json.dump(config, open(f"bank/{ctx.guild.name}.json", 'w'), indent = 4)
                        await ctx.message.add_reaction("✅")
                    except:
                        await ctx.send("金額輸入錯誤 請輸入整數")
                else:
                    await ctx.send("沒有指定金額")
                    await ctx.send("用法: ~bgive <@用戶> <金額>")
            else:     
                await ctx.send("沒有這個用戶 請確認他是否已經開戶")
                await ctx.send("用法: ~bgive <@用戶> <金額>")
        else:
            print(type(ctx.author.id))
            await ctx.send("你不是管理員 此指令只有管理員可以使用")
            await ctx.message.add_reaction("❌")

def setup(bot):
    bot.add_cog(bgive(bot))
    '''