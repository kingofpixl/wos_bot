import requests
from discord import Embed

my_steam_id = 76561198099909736


def get_my_wishlist(steam_id: str):

    steam_user_wishlist_url = "https://store.steampowered.com/wishlist/profiles/" + steam_id + "/wishlistdata/"
    try:
        response = requests.get(steam_user_wishlist_url)
    except requests.exceptions.RequestException or requests.exceptions:
        return 'The Users Wishlist Is Private'
    json_response = response.json()

    if len(json_response) == 1:
        return 'Please make sure your wishlist is set to public'

    wishlist_information = {}

    for key in json_response:
        if json_response[key]['subs'] and len(json_response[key]['subs']) != 0:
            wishlist_information[json_response[key]['name']] = show_as_price(json_response[key]['subs'][0]['price'])
        else:
            wishlist_information[json_response[key]['name']] = 'No Price Yet'

    if len(show_as_bullet_points(wishlist_information)) > 2000:
        return 'Your wishlist is too long, please wait whilst we look into showing your whole wishlist'

    return show_as_bullet_points(wishlist_information)


def show_as_price(price: str):
    return '$' + price[:-2] + '.' + price[-2:]


def show_as_bullet_points(wishlist: dict):
    return "\n".join(["* " + key + ': ' + value for key, value in wishlist.items()])

