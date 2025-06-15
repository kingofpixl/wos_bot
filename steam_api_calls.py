import os
from steam_web_api import Steam
from dotenv import load_dotenv

load_dotenv()
STEAM_KEY = os.getenv('STEAM_API_TOKEN')
steam = Steam(STEAM_KEY)


def get_user_profile(username: str):
    user = steam.users.search_user(username)
    print(user)


def get_game(user, game_name: str):
    game = steam.apps.search_games(term=game_name, country='CA')
    return f'hello {user.mention} {game['apps'][0]['name']} is {game['apps'][0]['price']}'

# your id: 76561198061247902
def recently_played_games(user_id):
    recent_games = steam.users.get_user_recently_played_games(user_id)['games']
    list_of_recent_games = []
    games_played = f'here are the users recently played games: '

    for game in recent_games:
        list_of_recent_games.append(f"{game.get('name')} for {round(float(int(game.get('playtime_2weeks')) / 60), 2)} hours")

    empty_string = ', '.join(list_of_recent_games)

    games_played += empty_string

    return games_played
