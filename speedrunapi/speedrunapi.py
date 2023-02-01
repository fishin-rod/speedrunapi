from json import loads
from urllib.request import urlopen
from functools import lru_cache
import urllib.error
from speedrunapi.errors import URLerror
#start doing error handleing here

class User_Requests:
    """Makes the user requests to speedrun.com"""
    
    @lru_cache(maxsize = 10)  
    def user_reqest(self):
        """Makes a request to speedrun.com"""
        url = f'https://www.speedrun.com/api/v1/users?lookup={self.user}'
        responce = urlopen(url)
        self.user_data = loads(responce.read().decode('utf-8'))['data']
        return self.user_data

    @lru_cache(maxsize = 10)
    def user_data_request(self, x):
        """Makes a request to speedrun.com to get the full data of the user
        
        ARGS:
        x (int): The index of the link being retrieved"""
        self.user_stat_links()
        url = self.final_links[x]
        responce = urlopen(url)
        self.user_data_response = loads(responce.read().decode('utf-8'))['data']
        return self.user_data_response
            
    @lru_cache(maxsize = 10)
    def user_stat_links(self):
        """Returns the links for the users other pages such as their runs,personal bests, etc. As a list"""
        self.final_links = []
        link_types = ['self', 'runs', 'games', 'personal-bests']
        for link_type in range(len(link_types)):
            self.final_links.append(self.user_data[0]['links'][link_type]['uri'])
        return self.final_links
    
    def __init__(self, user):
        self.user = user
        self.user_reqest()
        
class Game_Requests:
    """Makes the game requests to speedrun.com"""
    
    @lru_cache(maxsize = 10)  
    def game_reqest_quick(self):
        """Makes a request to speedrun.com just to get the nessiisary info to do a better query"""
        url = f'https://www.speedrun.com/api/v1/games?name={self.game}'
        response = urlopen(url)
        self.quick_game_data = loads(response.read().decode('utf-8'))
        return self.quick_game_data
    
    @lru_cache(maxsize = 10)
    def game_request(self):
        """Makes a request to speedrun.com to get the nessisary info to do a better query"""
        url = f'https://www.speedrun.com/api/v1/games/{self.game}'
        responce = urlopen(url)
        self.game_data = loads(responce.read().decode('utf-8'))['data']
        return self.game_data
    
    @lru_cache(maxsize = 10)
    def game_data_request(self, x):
        """Uses the links in user_stat_links to retrieve different data for more specific topics
        ARGS:
        x (int): The index of the link in the user_stat_links list"""
        self.game_stat_links()
        url = self.final_links[x]
        responce = urlopen(url)
        self.game_data_response = loads(responce.read().decode('utf-8'))['data']
        return self.game_data_response
    
    @lru_cache(maxsize = 10)
    def game_stat_links(self):
        """Returns the links for the runs, levels, etc. for the game as a list"""
        self.final_links = []
        link_types = ['self', 'runs', 'levels', 'catagories', 'variables', 'records', 'series', 'base-game', 'derived-games', 'romhacks', 'leaderboard']
        for link_type in range(len(link_types)-1):
            self.final_links.append(self.game_data['links'][link_type]['uri'])
        return self.final_links

    def __init__(self, game):
        self.game = game

class Misc_Requests:

    @lru_cache(maxsize = 10)
    def region_data_request(url):
        """Returns the data for regions after provideing a url to get it"""
        response = urlopen(url) #type: ignore python cant see the url supplied as a parmater
        region_data = loads(response.read().decode('utf-8'))['data']
        return region_data

    @lru_cache(maxsize = 10)
    def region_link_request(region, x):
        """Gets the links for the region data
        ARGS:
        x (int): The index of the link to get"""
        region = region.split(' ', 1)[0] #type: ignore ,error with python thinking its a callable value when its not
        try:
            url = f'https://www.speedrun.com/api/v1/regions/{region}'
        except urllib.error.HTTPError:
            try: 
                url = f'https://www.speedrun.com/api/v1/games?region={region}'
            except urllib.error.HTTPError:
                raise URLerror("Invalid region")
        responce = urlopen(url)
        region_data = loads(responce.read().decode('utf-8'))['data']['links'][x]['uri']
        return region_data
    
    @lru_cache(maxsize = 10)
    def leaderboard_data_request(url):
        """Returns data for leaderboards on speedrun.com"""
        try:
            response = urlopen(url) #type: ignore
            leaderboard_data = loads(response.read().decode('utf-8'))['data']
        except urllib.error.HTTPError:
            raise URLerror("Invalid game or category")
        return leaderboard_data
