# cogs/todo.py

import discord
from discord.ext import commands
from core.any import Cog_Extension

class todo(Cog_Extension):
    @commands.command()
    @commands.is_owner()
    async def todo(self, ctx, *arg):
        if not arg:
            await ctx.send("請輸入指令")

        elif arg[0].upper() == "ADD":
            if len(arg) == 1:
                await ctx.send("請輸入內容")
            else:
                with open("todo.txt", 'a', encoding="UTF-8") as f:
                    f.write(f"{arg[1]}\n")
                await ctx.send("已新增")

        elif arg[0].upper() == "DEL":
            if len(arg) == 1:
                await ctx.send("請輸入內容")
            else:
                with open("todo.txt", 'r', encoding="UTF-8") as f:
                    lines = f.readlines()
                with open("todo.txt", 'w', encoding="UTF-8") as f:
                    for line in lines:
                        if line.strip() != arg[1]:
                            f.write(line)
                await ctx.send("已刪除")

        elif arg[0].upper() == "LIST":
            with open("todo.txt", 'r', encoding="UTF-8") as f:
                lines = f.readlines()
            await ctx.send("\n".join(lines))

        elif arg[0].upper() == "EDIT":
            if len(arg) == 1:
                await ctx.send("請輸入內容")
            else:
                if len(arg) == 2:
                    await ctx.send("請輸入修改內容")
                else:
                    with open("todo.txt", 'r', encoding="UTF-8") as f:
                        lines = f.readlines()
                    with open("todo.txt", 'w', encoding="UTF-8") as f:
                        for line in lines:
                            if line.strip() != arg[1]:
                                f.write(line)
                    with open("todo.txt", 'a', encoding="UTF-8") as f:
                        f.write(f"{arg[2]}\n")
                    await ctx.send("已修改")
    
    @commands.command()
    async def todolist(self, ctx):
        with open("todo.txt", 'r', encoding="UTF-8") as f:
            lines = f.readlines()
        await ctx.send("\n".join(lines))

def setup(bot):
    bot.add_cog(todo(bot))