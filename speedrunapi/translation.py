from json import loads
from urllib.request import urlopen
import urllib.error
import http.client
from functools import lru_cache
from speedrunapi.errors import URLerror
#try to make just one request or just a couple of requests

@lru_cache()
def username_to_id(name):
    """Turns a username of a player on speedrun.com into the id of that player"""
    try:
        url = f'https://www.speedrun.com/api/v1/users?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['id']
    except IndexError:
        return "No name found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nNames cannot contain a non alphanumeric character')

@lru_cache()    
def game_name_to_id(name):
    """Turns a game name of a player on speedrun.com into the id of that game"""
    try:
        name = name.replace(' ','_')
        url = f'https://www.speedrun.com/api/v1/games?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['id']
    except IndexError:
        return "No game found"

@lru_cache()   
def game_name_to_abbreviation(name):
    """Turns a game name of a player on speedrun.com into the abbreviation of that game"""
    try:
        name=name.replace(' ','_')
        url = f'https://www.speedrun.com/api/v1/games?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['abbreviation']
    except IndexError:
        return "No game found"

@lru_cache()
def category_name_to_id(game, category_name):
    """Turns a name of a category into an id
    
    ARGS:
        game (str): The name of the game
        category_name (str): The name of the category"""
    from speedrunapi import Categories
    try:
        category_data = Categories(game)
        for category in range(len(category_data.category_names)):
            if category_data.category_names[category].lower() == category_name.lower():
                return category_data.category_ids[category]
    except IndexError:
        return "No category found"

@lru_cache()
def translate_user_id(userid):
    """Turns a user id of a user into the username of the user"""
    try:
        url = f'https://www.speedrun.com/api/v1/users/{userid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No user found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nIDs cannot contain a non alphanumeric character')

@lru_cache()  
def translate_game_id(gameid):
    """Turns a game id of a game into the name of the game"""
    try:
        url = f'https://www.speedrun.com/api/v1/games/{gameid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No game found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nIDs cannot contain a non alphanumeric character')

@lru_cache()   
def translate_game_abbreviation(game_abbreviation):
    """Turns the game abbreviation of a game into the name of the game"""
    try:
        url = f'https://www.speedrun.com/api/v1/games/{game_abbreviation}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No game found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nAbbreviations cannot contain a non alphanumeric character')

@lru_cache()   
def translate_region(regionid):
    """Turns the region id of a region into the name of the region
    
    ARGS:
        regionid (str): The id of the region"""
    try:
        url = f'https://www.speedrun.com/api/v1/regions/{regionid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No region found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nregion IDs cannot contain a non alphanumeric character')

@lru_cache()    
def translate_platform(platformid):
    """Turns the platform id of a platform into the name of the platform"""
    try:
        url = f'https://www.speedrun.com/api/v1/platforms/{platformid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No platform found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nplatform IDs cannot contain a non alphanumeric character')

@lru_cache()   
def translate_genre(genreid):
    """Turns the genre id of a genre into the name of the genre"""
    try:
        url = f'https://www.speedrun.com/api/v1/genres/{genreid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No genre found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\ngenre IDs cannot contain a non alphanumeric character')

@lru_cache()   
def translate_engine(engineid):
    """Turns the engine id of a engine into the name of the engine"""
    try:
        url = f'https://www.speedrun.com/api/v1/engines/{engineid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No engine found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nengine IDs cannot contain a non alphanumeric character')

@lru_cache()
def translate_level(levelid):
    """Turns the level id of a level into the name of the level"""
    try:
        url = f'https://www.speedrun.com/api/v1/levels/{levelid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No level found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nlevel IDs cannot contain a non alphanumeric character')

@lru_cache()
def translate_category(categoryid):
    """Turns the category id of a category into the name of the category
    
    ARGS:
    categoryID: the id of the category"""
    try:
        url = f'https://www.speedrun.com/api/v1/categories/{categoryid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No category found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\ncategory IDs cannot contain a non alphanumeric character')

@lru_cache()
def translate_variable(variableid):
    """Turns the variable id of a variable into the name of the variable"""
    try:
        url = f'https://www.speedrun.com/api/v1/variables/{variableid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No variable found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nvariable IDs cannot contain a non alphanumeric character')

@lru_cache()   
def translate_level_id(levelid):
    """Turns the level id of a level into the name of the level"""
    try:
        url = f'https://www.speedrun.com/api/v1/levels/{levelid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No level found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nlevel IDs cannot contain a non alphanumeric character')
