import os
from steam_web_api import Steam
from dotenv import load_dotenv

load_dotenv()
STEAM_KEY = os.getenv('STEAM_API_TOKEN')
steam = Steam(STEAM_KEY)


def get_user_profile(username: str):
    user = steam.users.search_user(username)
    print(user)

def get_game(game: str):
    game = steam.apps.search_games(term="divinity", country='CA')
    print(game)
    print(game['apps'][0]['name'])
