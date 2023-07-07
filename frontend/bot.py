import discord
import requests
import json
from discord.ext import commands

def run_discord_bot():
    TOKEN = 'MTEyNTQwODgzNzQ5NTY5NzQ3OA.Gnz-jn.ToZiULAY7zDKPBI6ifv8Zg49CJauoq-20AyUVA'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    client = commands.Bot(command_prefix='-', intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is ready.')

    @client.command()
    async def helper(ctx):
        embed = discord.Embed(title="Contest Seeker", description="Bot Command line", color=0x00FFFF)
        commandArray = list()
        funcArray = list()
        funcArray.append("To create leaderboard")
        funcArray.append("To get leaderboard")
        funcArray.append("To add an userID in leaderboard")
        funcArray.append("To delete an userID in leaderboard")
        commandArray.append("-leaderboard create")
        commandArray.append("-leaderboard show <LEADERBOARD_ID>")
        commandArray.append("-leaderboard add <LEADERBOARD_ID> <USER_ID>")
        commandArray.append("-leaderboard delete <LEADERBOARD_ID> <USER_ID>")
        l = len(commandArray)
        for i in range(l):
            embed.add_field(
                name=f'***#{i+1}***', value=f'*{funcArray[i]}*  ➤ `{commandArray[i]}`', inline=False)
        await ctx.send(embed=embed)

    @client.command()
    async def leaderboard(ctx, *args):
        if args[0] == "create":
            tempData = requests.post(f'https://contest-seeker.onrender.com/api/leaderboard/create')
            tempData = tempData.json()
            embed = show(tempData['id'])
            await ctx.send(embed=embed)
        elif args[0] == "add":
            data = {
                "user": args[2],
            }
            tempData = requests.put(f'https://contest-seeker.onrender.com/api/leaderboard/add/{args[1]}', json=data)
            embed = show(args[1])
            await ctx.send(embed=embed)
        elif args[0] == "show":
            embed = show(args[1])
            await ctx.send(embed=embed)
        elif args[0] == "delete":
            data = {
                "user": args[2],
            }
            tempData = requests.delete(f'https://contest-seeker.onrender.com/api/leaderboard/delete/{args[1]}', json=data)
            embed = show(args[1])
            await ctx.send(embed=embed)
        else:
            await ctx.send("Not a valid command! USE '-helper' command.")

    client.run(TOKEN)

def show(id):
    tempData = requests.get(f'https://contest-seeker.onrender.com/api/leaderboard/get/{id}')
    tempData = tempData.json()
    embed = discord.Embed(title="LeaderBoard: "+ id, description="Members of LeaderBoard", color=0x00FFFF)
    userArray = list()
    ratingArray = list()
    titleArray = list()
    for element in tempData:
        userArray.append(element["user"])
        titleArray.append(element["rank"])
        ratingArray.append(element["rating"])
    
    l = len(userArray)
    memberList = []
    for i in range(l):
        tempList = list()
        tempList.append(ratingArray[i])
        tempList.append(userArray[i])
        tempList.append(titleArray[i])
        memberList.append(tempList)

    memberList.sort(reverse=True)
    for i in range(l):
        embed.add_field(
            name=f'***Rank #{i+1}***', value=f'*{memberList[i][1]}*  ➤ `{memberList[i][0]}` ➤ `{memberList[i][2]}`', inline=False)
    return embed
