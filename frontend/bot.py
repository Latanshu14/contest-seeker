import discord
import responses
from discord.ext import commands

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        print(response)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# async def send_msg(message, user_msg):
#     try:
#         response = responses.handle_response(user_msg)
#         message.author.send(response)
#     except Exception as e:
#         print(e)

def run_discord_bot():
    TOKEN = 'MTEyNTQwODgzNzQ5NTY5NzQ3OA.G6l2YI.w2VCZtsN-JRSeGa0VVquGXaQlqDhRspHLs2TPg'
    intents = discord.Intents.default()
    intents.message_content = True
    # intents = discord.Intents(messages=True, guilds=True)
    # intents.typing = False
    # intents.presences = False
    client = discord.Client(intents=intents)
    client = commands.Bot(command_prefix='-', intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is ready.')

    # @client.event
    @client.command()
    async def hi(ctx):
        await ctx.send("Hello!!")

    @client.command()
    async def happy(ctx, *args):
        await ctx.send("sexy" + args[0])

    @client.command()
    async def contest(ctx, *args):
        # gives upcoming contest
    
    @client.command()
    async def leaderboard(ctx, *args):
        # id
        # gives upcoming contest

    client.run(TOKEN)