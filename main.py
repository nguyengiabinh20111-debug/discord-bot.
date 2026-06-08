import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot đã online: {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Chào ní, mình là bot đây!')

client.run(os.environ['TOKEN'])
