from random import choice, randint

from steam_api_calls import get_user_profile, get_game, recently_played_games


def get_discord_response(user_input: str, user, server) -> str:
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
        return get_game(user, lowered[6:])
    elif 'recently played' in lowered:
        return recently_played_games(lowered[16:])
    elif 'server' in lowered:
        return f'{server} has the id: {server.id}'
    else:
        return choice([
            'I do not understand...',
            'What are you talking about?',
            'Do you mind rephrasing that?'
        ])
