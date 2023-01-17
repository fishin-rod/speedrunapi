from json import loads
from urllib.request import urlopen
import urllib.error
import http.client
from .errors import URLerror
#try to make just one request or just a couple of requests

def username_to_id(name):
    try:
        url = f'https://www.speedrun.com/api/v1/users?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['id']
    except IndexError:
        return "No name found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nNames cannot contain a non alphanumeric character')
    
def game_name_to_id(name):
    try:
        name=name.replace(' ','_')
        url = f'https://www.speedrun.com/api/v1/games?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['id']
    except IndexError:
        return "No game found"
    
def game_name_to_abbreviation(name):
    try:
        name=name.replace(' ','_')
        url = f'https://www.speedrun.com/api/v1/games?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['abbreviation']
    except IndexError:
        return "No game found"

def translate_user_id(userid):
    try:
        url = f'https://www.speedrun.com/api/v1/users/{userid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No user found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nIDs cannot contain a non alphanumeric character')
    
def translate_game_id(gameid):
    try:
        url = f'https://www.speedrun.com/api/v1/games/{gameid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No game found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nIDs cannot contain a non alphanumeric character')
    
def translate_game_abbreviation(game_abbreviation):
    try:
        url = f'https://www.speedrun.com/api/v1/games/{game_abbreviation}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No game found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nAbbreviations cannot contain a non alphanumeric character')
    
def translate_region(regionid):
    try:
        url = f'https://www.speedrun.com/api/v1/regions/{regionid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No region found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nregion IDs cannot contain a non alphanumeric character')
    
def translate_platform(platformid):
    try:
        url = f'https://www.speedrun.com/api/v1/platforms/{platformid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No platform found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nplatform IDs cannot contain a non alphanumeric character')
    
def translate_genre(genreid):
    try:
        url = f'https://www.speedrun.com/api/v1/genres/{genreid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No genre found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\ngenre IDs cannot contain a non alphanumeric character')
    
def translate_engine(engineid):
    try:
        url = f'https://www.speedrun.com/api/v1/engines/{engineid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No engine found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nengine IDs cannot contain a non alphanumeric character')

def translate_level(levelid):
    try:
        url = f'https://www.speedrun.com/api/v1/levels/{levelid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No level found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nlevel IDs cannot contain a non alphanumeric character')

def translate_catagory(catagoryid):
    try:
        url = f'https://www.speedrun.com/api/v1/categories/{catagoryid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No catagory found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\ncatagory IDs cannot contain a non alphanumeric character')

def translate_variable(variableid):
    try:
        url = f'https://www.speedrun.com/api/v1/variables/{variableid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No variable found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nvariable IDs cannot contain a non alphanumeric character')
    
def translate_level_id(levelid):
    try:
        url = f'https://www.speedrun.com/api/v1/levels/{levelid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No level found"
    except http.client.InvalidURL as e:
        details = e.args[0].split("'")[2]
        raise URLerror(f'{details}\nlevel IDs cannot contain a non alphanumeric character')
