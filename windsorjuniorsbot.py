import os
import random
import discord

from discord.ext import commands

TOKEN = 'NzkwNTYwOTkyODk0Nzc5NDEy.X-CZTA.J5B_JZmyPx3qfuLmGJcd61ysLEk'

data_list = [["SritejTummuru", "TeamSD", "O"]]

bot = commands.Bot(command_prefix='!')


@bot.command(name='register')
async def register(ctx, name: str, team: str, status: str):
    for person in data_list:
        if person[0] == name:
            if person[1] == team:
                if person[2] == status:
                    await ctx.send("You are registered successfully!")
                    data_list.remove(person)
                    break
                    
    print(len(data_list))

@bot.command(name='registration-status')
async def return_status(ctx):
    string_to_return = ""
    string_to_return += str(len(data_list)) + " people have not been registered:"
    for person in data_list:
        string_to_return += "\n" + person[0] + ", " + person[1]
    await ctx.send(string_to_return)

bot.run(TOKEN)
