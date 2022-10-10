import discord
import asyncio
import get_reply
import random
from random import randint

async def print_board(boards, ctx):
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
def random_row(board):
    return randint(0, len(board) - 3)

def random_col(board):
    return randint(0, len(board[0]) - 3)

async def battleship(ctx, client):
	Input = True
	verti_hori = randint(0,1)
	await ctx.channel.send("""What difficulty level would you like? 
		Type 'E' for Easy, 'M' for Medium or 'H' for Hard: """)
	diff = await get_reply.user_message(context=ctx, client=client, timeoutmsg= "Please try again")
	if diff == "e" or diff == "m" or diff == "h":
		board = []
		if diff == "e":
			for x in range(5):
				board.append(["O"] * 5)
				print(x)
		elif diff == "m":
			for x in range(7):
				board.append(["O"] * 7)
		elif diff == "h":
			for i in range(9):
				board.append(["O"] * 9)
		await ctx.channel.send("Battleship Board:")
		await print_board(boards=board, ctx=ctx)

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

			guess_row = await get_reply.user_message(context=ctx, client = client, timeoutmsg= "Please Try again")
			guess_row = int(guess_row)
			if guess_row != "":
				await ctx.channel.send("Type your guess column")
				guess_col = await get_reply.user_message(context=ctx, client = client, timeoutmsg= "Please Try again")
			guess_col = int(guess_col)

			if ((guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)) and diff == "e":
				await ctx.channel.send("oops that's not even in the ocean")
				Ocean = False
				turn += 1
			if ((guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6)) and diff == "m":
				await ctx.channel.send("oops that's not even in the ocean")
				Ocean = False
				turn += 1
			if ((guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 8)) and diff == "h":
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
					await print_board(ctx = ctx, boards = board)
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
					await print_board(ctx = ctx, boards = board)
					await ctx.channel.send("Congratulations! You sunk my battleship!")
					break
			else:
				if miss and Ocean:
					await ctx.channel.send("You Missed")
					board[guess_row][guess_col] = "X"
					turn += 1
			await print_board(ctx = ctx, boards = board)
			if turn == maxturns:
				await ctx.channel.send("Game Over")
				break

