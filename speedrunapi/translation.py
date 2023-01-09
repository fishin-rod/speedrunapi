from json import loads
from urllib.request import urlopen
import urllib.error

def username_to_id(name):
    try:
        url = f'https://www.speedrun.com/api/v1/users?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['id']
    except IndexError:
        return "No name found"

def game_name_to_id(name):
    try:
        name=name.replace(' ','_')
        url = f'https://www.speedrun.com/api/v1/games?name={name}'
        return loads(urlopen(url).read().decode('utf-8'))['data'][0]['id']
    except IndexError:
        return "No game found"

def translate_user_id(userid):
    try:
        url = f'https://www.speedrun.com/api/v1/users/{userid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No user found"
    
def translate_game_id(gameid):
    try:
        url = f'https://www.speedrun.com/api/v1/games/{gameid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No game found"
    
def translate_game_abbreviation(game_abbreviation):
    try:
        url = f'https://www.speedrun.com/api/v1/games/{game_abbreviation}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['names']['international'] 
    except urllib.error.HTTPError:
        return "No game found"
    
def translate_region(regionid):
    try:
        url = f'https://www.speedrun.com/api/v1/regions/{regionid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No region found"
    
def translate_platform(platformid):
    try:
        url = f'https://www.speedrun.com/api/v1/platforms/{platformid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No platform found"
    
def translate_genre(genreid):
    try:
        url = f'https://www.speedrun.com/api/v1/genres/{genreid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No genre found"
    
def translate_engine(engineid):
    try:
        url = f'https://www.speedrun.com/api/v1/engines/{engineid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No engine found"

def translate_level(levelid):
    try:
        url = f'https://www.speedrun.com/api/v1/levels/{levelid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No level found"

def translate_catagory(catagoryid):
    try:
        url = f'https://www.speedrun.com/api/v1/categories/{catagoryid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No catagory found"

def translate_variable(variableid):
    try:
        url = f'https://www.speedrun.com/api/v1/variables/{variableid}'
        return loads(urlopen(url).read().decode('utf-8'))['data']['name']
    except urllib.error.HTTPError:
        return "No variable found"
