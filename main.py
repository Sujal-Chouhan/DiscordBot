import asyncio
from datetime import time
from battleship import battleship
import get_reply
import discord
import random
import rockpaperscissors
from random import randint
from googlesearch import search

# Rock Paper Scissors Computer Options:
rpsgame = ("rock", "paper", 'scissors')

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(ctx):
    username = str(ctx.author).split("#")[0]
    user_message = str(ctx.content)
    channel = str(ctx.channel.name)
    print(f"{username}: {user_message} ({channel})")
    if ctx.author == client.user:
        return

    if ctx.channel.name == "bot":
        if user_message.lower() == "hello":
            await ctx.channel.send(f"Hello {username}!")
            return
        elif user_message.lower() == "bye":
            await ctx.channel.send(f"Bye {username}!")
            return
        elif user_message.lower() == "!random":
            response = f"This is your random number: {random.randrange(1000000)}"
            await ctx.channel.send(response)
            return
        # ROCK PAPER SCISSORS CODE STARTS HERE #
        elif user_message.lower() == "!rps":
            await rockpaperscissors.rps_run(ctx=ctx,client=client)
            return        
        # BATTLESHIP CODE STARTS HERE #
        elif user_message.lower().startswith("!bs"):
            await battleship(ctx=ctx, client=client)
            return
        # GOOGLE SEARCH CODE STARTS HERE #
        elif user_message.lower().startswith("!google"):
            for result in search(term=user_message[8::], num_results=4, advanced=False):
                await ctx.channel.send(f"{result}")
            return
client.run(TOKEN)
