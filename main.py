import os
from datetime import datetime

from typing import Final

import aiocron
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv
from discord import Intents, Message, Embed
from discord.ext import commands, tasks
from responses import get_discord_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
PERSONAL_SERVER_ID = os.getenv('PERSONAL_SERVER_ID')

# STEP 1: BOT SETUP
intents = Intents.default()
intents.message_content = True # NOQA (no quality assurance)
client = commands.Bot(command_prefix='!', intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str, username, server) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    is_private = user_message[0] == '?'

    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_discord_response(user_message, user=username, server=server)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)


async def weekly_message():
    channel = client.get_channel(1249446467979182122)
    await channel.send("howdy there partner")


# STEP 3: HANDLING STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

    scheduler = AsyncIOScheduler()

    scheduler.add_job(weekly_message, CronTrigger(day_of_week="sat", hour="20", minute="38", second="0"))

    scheduler.start()


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    username = message.author
    user_message: str = message.content
    channel: str = str(message.channel)
    server = message.guild

    if message.content.startswith("embed dnd"):
        dnd_class = message.content[10:]
        embed = Embed(title=dnd_class, url="http://dnd5e.wikidot.com/" + dnd_class, description='class info', color=0xFFA500)
        await message.channel.send(embed=embed)
        return
    elif message.content.startswith("embed bb"):
        embed = Embed(title="Business Base", url="https://businessbase.ca/", description='we at the business base', color=0xFFA500)
        await message.channel.send(embed=embed)
        return

    print(f'[{channel}] {str(username)}: "{user_message} on {server}")')
    await send_message(message, user_message, username, server)

# STEP 5: MAIN ENTRY POINT
client.run(token=DISCORD_TOKEN)
