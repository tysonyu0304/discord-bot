# cogs/extension.py

from discord.ext import commands
from core.any import Cog_Extension

class extension(Cog_Extension):
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *arg):
        if arg:
            try:
                self.bot.load_extension(f"cogs.{arg[0]}")
                await ctx.message.add_reaction("✅")
            except:
                await ctx.send("沒有這個模組")
                await ctx.message.add_reaction("❌")
        else:
            await ctx.send("沒有指定模組 請在指令後面直接輸入模組名稱")
            await ctx.message.add_reaction("❌")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *arg):
        if arg:
            try:
                self.bot.unload_extension(f"cogs.{arg[0]}")
                await ctx.message.add_reaction("✅")
            except:
                await ctx.send("沒有這個模組")
                await ctx.message.add_reaction("❌")
        else:
            await ctx.send("沒有指定模組 請在指令後面直接輸入模組名稱")
            await ctx.message.add_reaction("❌")
    
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *arg):
        if arg:
            try:
                self.bot.reload_extension(f"cogs.{arg[0]}")
                await ctx.message.add_reaction("✅")
            except:
                await ctx.send("沒有這個模組")
                await ctx.message.add_reaction("❌")
        else:
            await ctx.send("沒有指定模組 請在指令後面直接輸入模組名稱")
            await ctx.message.add_reaction("❌")

def setup(bot):
    bot.add_cog(extension(bot))