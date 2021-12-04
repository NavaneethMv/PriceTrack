import asyncio
from discord.ext import tasks
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import scrape

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord")


@bot.command()
async def track(ctx, link: str, time = 60):
    global tracking


    @tasks.loop(seconds=time)
    async def tracking(ctx):
        title, price = scrape.scrape(link)
        await ctx.send(title)
        await ctx.send(price)
        await asyncio.sleep(time)
    

    tracking.start(ctx)
    await ctx.send("Tracking prices..")


@bot.command()
async def stop(ctx):
    tracking.cancel()
    await ctx.send("Tracking stopped")


bot.run(TOKEN)