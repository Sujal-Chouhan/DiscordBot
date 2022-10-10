import discord
import asyncio

async def user_message(context, client, timeoutmsg):
	try:
		reply = await client.wait_for("message", check=lambda m: m.author == context.author and
                                                                                  m.channel == context.channel, timeout=30.0)
	except asyncio.TimeoutError:
		await context.channel.send(timeoutmsg)
	
	return str(reply.content.lower())
