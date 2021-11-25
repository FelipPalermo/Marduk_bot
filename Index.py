import discord
from CommandHandler import CommandHandler


client = discord.Client()
token = 'NTg0MDExMTM4MDEwNzEwMDQ2.XPEswQ.PlzUk1687busl--vNl55E1is2UE'

@client.event
async def on_ready():
    print('Logada e preparada')

ch = CommandHandler(client)

client.run(token)