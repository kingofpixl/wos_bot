from random import choice, randint
from discord import Embed
from steam_api_calls import get_user_profile, get_game, recently_played_games


def get_discord_response(user_input: str, user=None) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "well, you\'re awfully silent..."
    elif 'hello' in lowered:
        return f'Hello there {user.mention}'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'steam' in lowered:
        return get_game(lowered[6:], user)
    elif 'recently played' in lowered:
        return recently_played_games(lowered[16:])
    elif 'embed' in lowered:
        return 'no embed yet'
    else:
        return choice([
            'I do not understand...',
            'What are you talking about?',
            'Do you mind rephrasing that?'
        ])
