import requests
from discord import Embed
import os
from steam_web_api import Steam
from dotenv import load_dotenv

load_dotenv()

my_steam_id = 76561198099909736
STEAM_KEY = os.getenv('STEAM_API_TOKEN')

def get_my_wishlist(steam_id: str):
    # "http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v1/?key=1234567890&steamid=000123000456"
    steam_user_wishlist_url = "https://api.steampowered.com/IWishlistService/GetWishlist/v1/?steamid=" + steam_id
    print(steam_user_wishlist_url)
    try:
        response = requests.get(steam_user_wishlist_url)
    except requests.exceptions.RequestException or requests.exceptions:
        return 'The Users Wishlist Is Private'
    json_response = response.json()
    print(json_response)

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

