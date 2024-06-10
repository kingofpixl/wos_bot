import os

from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message, Member
from responses import get_discord_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
PERSONAL_SERVER_ID = os.getenv('PERSONAL_SERVER_ID')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True # NOQA (no quality assurance)
client: Client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    is_private = user_message[0] == '?'
    server = 

    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_discord_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}")')
    await send_message(message, user_message)

# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=DISCORD_TOKEN)

if __name__ == '__main__':
    main()
