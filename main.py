import asyncio

import discord
import random
from random import randint
from googlesearch import search

# Rock Paper Scissors Computer Options:
rpsgame = ("rock", "paper", 'scissors')

TOKEN = ""

client = discord.Client()


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
            while True:
                computer_guess = str(random.choice(rpsgame))

                embed = discord.Embed(title="Rock Paper Scissors", description="Type one of the following:", colour=discord.Colour.green())
                embed.add_field(name="Rock\nPaper\nScissors", value="NO CHEATING")

                await ctx.channel.send(embed=embed)
                try:
                    rps_choice = await client.wait_for("message", check=lambda m: m.author == ctx.author and
                                                                                  m.channel == ctx.channel, timeout=30.0)
                # In case user does not respond #
                except asyncio.TimeoutError:
                    await ctx.channel.send("Too Scared to play? Fine, I'll take that as a win")
                    break
                # All Possible Scenarios of Rock Paper Scissors #
                else:
                    if rps_choice.content.lower() == "rock":
                        if computer_guess == "paper":
                            await ctx.channel.send(f"HAHA YOU LOSE I CHOSE PAPER {ctx.author.mention}" )
                        if computer_guess == "rock":
                            await ctx.channel.send(f"It's a Tie, I also chose rock {ctx.author.mention}")
                        if computer_guess == "scissors":
                            await ctx.channel.send(f"Damn I lost I chose scissors :( {ctx.author.mention}")
                    elif rps_choice.content.lower() == "paper":
                        if computer_guess == "paper":
                            await ctx.channel.send(f"It's a Tie, I also chose paper {ctx.author.mention}")
                        if computer_guess == "rock":
                            await ctx.channel.send(f"Damn I lost I chose rock :( {ctx.author.mention}")
                        if computer_guess == "scissors":
                            await ctx.channel.send(f"HAHA YOU LOSE I CHOSE SCISSORS {ctx.author.mention}")
                    elif rps_choice.content.lower() == "scissors":
                        if computer_guess == "paper":
                            await ctx.channel.send(f"Damn I lost I chose paper :( {ctx.author.mention}")
                        if computer_guess == "rock":
                            await ctx.channel.send(f"HAHA YOU LOSE I CHOSE ROCK {ctx.author.mention}")
                        if computer_guess == "scissors":
                            await ctx.channel.send(f"It's a Tie, I also chose scissors {ctx.author.mention}")
                    # Ensures While Loop Keeps Going Unless Player Wants To Stop #
                    try:
                        await ctx.channel.send("Type 'Yes' if you would like to play again")
                        play_again = await client.wait_for("message", check=lambda m: m.author == ctx.author and
                                                                                  m.channel == ctx.channel, timeout=30.0)
                    except asyncio.TimeoutError:
                        break
                    else:
                        if play_again.content.lower() != "yes":
                            break
        # BATTLESHIP CODE STARTS HERE #
        elif user_message.lower().startswith("!bs"):
            Input = True
            await ctx.channel.send("""
            What difficulty level would you like?
Type 'E' for Easy, 'M' for Medium or 'H' for Hard: """)

            try:
                diff = await client.wait_for('message',check=lambda m: m.author == ctx.author and
                                                                              m.channel == ctx.channel, timeout=30.0)
            except asyncio.TimeoutError:
                await ctx.channel.send("Please try again")
            else:
                # MAIN GAME STARTS HERE#
                # BOARD CREATION #
                if diff.content.lower() == "e" or diff.content.lower() == "m" or diff.content.lower () == "h":
                        board = []
                        if diff.content.lower() == "e":
                            for x in range(5):
                                board.append(["O"] * 5)
                                print(x)
                        elif diff.content.lower() == "m":
                            for x in range(7):
                                board.append(["O"] * 7)
                        elif diff.content.lower() == "h":
                            for i in range(9):
                                board.append(["O"] * 9)

                        async def print_board(boards):
                            bs_msg = ""
                            for row in boards:
                                " ".join(row)
                            for row in boards:
                                for tile in row:
                                    if tile == "O":
                                        bs_msg += "🟦"
                                    elif tile == "X":
                                        bs_msg += "⬜"
                                    elif tile == "!":
                                        bs_msg += "❌"
                                bs_msg += "\n"
                            await ctx.channel.send(bs_msg)

                        await ctx.channel.send("Battleship Board:")
                        await print_board(board)

                        def random_row(boards):
                            return randint(0, len(board) - 3)

                        def random_col(boards):
                            return randint(0, len(board[0]) - 3)
                        # Randomly Chooses To Either Create A Vertical or Horizontal Ship #
                        verti_hori = randint(0,1)
                        if verti_hori == 0:
                            ship_row1 = random_row(board)
                            ship_row = ship_row1
                            ship_coltemp = int(random_col(board))
                            ship_col1 = ship_coltemp
                            ship_col2 = ship_coltemp + 1
                            ship_col3 = ship_coltemp + 2
                            ship_col = (ship_col1, ship_col2, ship_col3)
                        if verti_hori == 1:
                            ship_row_temp = random_row(board)
                            ship_row1 = ship_row_temp
                            ship_row2 = ship_row_temp + 1
                            ship_row3 = ship_row_temp + 2
                            ship_col1 = random_col(board)
                            ship_col = ship_col1
                            ship_row = (ship_row1, ship_row2, ship_row3)
                        await ctx.channel.send(f"Cheat Row: {ship_row} Column: {ship_col}")

                        ######################################################################################
                        Ocean = True
                        miss = True
                        Hit = True
                        Ship = 0
                        turn = 1
                        maxturns = 6
                        while turn < maxturns:
                            Ocean = True
                            miss = True
                            Hit = True
                            await ctx.channel.send(f"Turn: {turn}")
                            await ctx.channel.send("Type your guess row")
                            try:
                                guess_row = await client.wait_for('message', check= lambda m: m.author == ctx.author
                                                                            and m.channel == ctx.channel,timeout = 30.0)
                            except asyncio.TimeoutError:
                                break
                            else:
                                guess_row = int(guess_row.content)
                                await ctx.channel.send("Type your guess column")
                                try:
                                    guess_col = await client.wait_for('message', check=lambda m: m.author == ctx.author
                                                                      and m.channel == ctx.channel, timeout= 30.0)
                                except asyncio.TimeoutError:
                                    break
                                else:
                                    guess_col = int(guess_col.content)
                                    if ((guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)) and diff.content.lower() == "e":
                                        await ctx.channel.send("oops that's not even in the ocean")
                                        Ocean = False
                                        turn += 1
                                    if ((guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6)) and diff.content.lower() == "m":
                                        await ctx.channel.send("oops that's not even in the ocean")
                                        Ocean = False
                                        turn += 1
                                    if ((guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 8)) and diff.content.lower() == "h":
                                        await ctx.channel.send("oops that's not even in the ocean")
                                        Ocean = False
                                        turn += 1
                                    if Ocean and ((board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!")):
                                        await ctx.channel.send("You guessed that one already")
                                        turn += 1
                                    elif verti_hori == 0 and guess_row == ship_row1 and (guess_col == ship_col1 or guess_col == ship_col2 or guess_col == ship_col3):
                                        await ctx.channel.send("Congratulations! You hit my battleship!")
                                        board[guess_row][guess_col] = "!"
                                        miss = False
                                        turn += 1
                                        maxturns += 1
                                        Ship = Ship + 1
                                        if Ship == 3:
                                            await print_board(board)
                                            await ctx.channel.send("Congratulations! You sunk my battleship!")
                                            break
                                    elif verti_hori == 1 and guess_col == ship_col1 and \
                                         (guess_row == ship_row1 or guess_row == ship_row2 or guess_row == ship_row3):
                                        await ctx.channel.send("Congratulations! You hit my battleship!")
                                        board[guess_row][guess_col] = "!"
                                        miss = False
                                        turn += 1
                                        maxturns += 1
                                        Ship += 1
                                        if Ship == 3:
                                            await print_board(board)
                                            await ctx.channel.send("Congratulations! You sunk my battleship!")
                                            break
                                    else:
                                        if miss and Ocean:
                                            await ctx.channel.send("You Missed")
                                            board[guess_row][guess_col] = "X"
                                            turn += 1
                                    await print_board(board)
                                    if turn == maxturns:
                                        await ctx.channel.send("Game Over")
                                        break
                else:
                    await ctx.channel.send("Please try again and enter a valid difficulty level")
        # GOOGLE SEARCH CODE STARTS HERE #
        elif user_message.lower().startswith("!google"):
            for result in search(query=user_message[8::], tld="com", num=1, stop=7, pause=2):
                await ctx.channel.send(f"{result}")

client.run(TOKEN)
