from random import randint
import discord
import random
import get_reply

rps_game = ("rock", "paper", "scissors")

async def rps_run(ctx, client,choices=rps_game):

    while True:
        computer_guess = str(random.choice(choices))

        embed = discord.Embed(title="Rock Paper Scissors", description="Type one of the following:", colour=discord.Colour.green())
        embed.add_field(name="Rock\nPaper\nScissors", value="NO CHEATING")

        await ctx.channel.send(embed=embed)
        rps_choice = await get_reply.user_message(context=ctx, client=client, timeoutmsg="Too scared to play? Fine, I'll take that as a win")

        # All Possible Scenarios of Rock Paper Scissors #
        if rps_choice == "rock":
            if computer_guess == "paper":
                await ctx.channel.send(f"HAHA YOU LOSE I CHOSE PAPER {ctx.author.mention}" )
            if computer_guess == "rock":
                await ctx.channel.send(f"It's a Tie, I also chose rock {ctx.author.mention}")
            if computer_guess == "scissors":
                await ctx.channel.send(f"Damn I lost I chose scissors :( {ctx.author.mention}")
        elif rps_choice == "paper":
            if computer_guess == "paper":
                await ctx.channel.send(f"It's a Tie, I also chose paper {ctx.author.mention}")
            if computer_guess == "rock":
                await ctx.channel.send(f"Damn I lost I chose rock :( {ctx.author.mention}")
            if computer_guess == "scissors":
                await ctx.channel.send(f"HAHA YOU LOSE I CHOSE SCISSORS {ctx.author.mention}")
        elif rps_choice == "scissors":
            if computer_guess == "paper":
                await ctx.channel.send(f"Damn I lost I chose paper :( {ctx.author.mention}")
            if computer_guess == "rock":
                  await ctx.channel.send(f"HAHA YOU LOSE I CHOSE ROCK {ctx.author.mention}")
            if computer_guess == "scissors":
                await ctx.channel.send(f"It's a Tie, I also chose scissors {ctx.author.mention}")

        # Ensures While Loop Keeps Going Unless Player Wants To Stop #
        await ctx.channel.send("Type 'Yes' if you would like to play again")
        play_again = await get_reply.user_message(context = ctx,client=client,timeoutmsg="Bye!")
        if play_again != "yes":
            break

