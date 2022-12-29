from json import loads
from urllib.request import urlopen
from functools import lru_cache
class User_Requests:
    """Makes the user requests to speedrun.com"""
    
    @lru_cache(maxsize=10)  
    def user_reqest(self):
        """Makes a request to speedrun.com"""
        url = f'https://www.speedrun.com/api/v1/users?lookup={self.user}'
        responce = urlopen(url)
        self.user_data = loads(responce.read().decode('utf-8'))['data']
        return self.user_data

    @lru_cache(maxsize=10)
    def user_data_request(self, x):
        """Makes a request to speedrun.com to get the full data of the user"""
        self.user_stat_links()
        url = self.final_links[x]
        responce = urlopen(url)
        self.user_data_response = loads(responce.read().decode('utf-8'))
        return self.user_data_response
            
    @lru_cache(maxsize=10)
    def user_stat_links(self):
        """Returns the links for the users other pages such as their runs,personal bests, etc. As a list"""
        self.final_links = []
        link_types = ['self', 'runs', 'games', 'personal-bests']
        for link_type in range(len(link_types)):
            self.final_links.append(self.user_data[0]['links'][link_type]['uri'])
        return self.final_links
    
    def __init__(self, user = str('')):
        self.user = user
        self.user_reqest()

class Game_Requests:
    """Makes the game requests to speedrun.com"""
    
    @lru_cache(maxsize=10)  
    def game_reqest_quick(self):
        """Makes a request to speedrun.com just to get the nessiisary info to do a better query"""
        url = f'https://www.speedrun.com/api/v1/games?name={self.game}'
        response = urlopen(url)
        self.quick_game_data = loads(response.read().decode('utf-8'))
        return self.quick_game_data
    
    @lru_cache(maxsize=10)
    def game_request(self):
        """Makes a request to speedrun.com to get the nessisary info to do a better query"""
        url = f'https://www.speedrun.com/api/v1/games/{self.game}'
        responce = urlopen(url)
        self.game_data = loads(responce.read().decode('utf-8'))['data']
        return self.game_data
    
    @lru_cache(maxsize=10)
    def game_data_request(self, x):
        """Uses the links in user_stat_links to retrieve different data for more specific topics"""
        self.game_stat_links()
        url = self.final_links[x]
        responce = urlopen(url)
        self.game_data_response = loads(responce.read().decode('utf-8'))['data']
        return self.game_data_response
    
    @lru_cache(maxsize=10)
    def game_stat_links(self):
        """Returns the links for the runs, levels, etc. for the game as a list"""
        self.final_links = []
        link_types = ['self', 'runs', 'levels', 'catagories', 'variables', 'records', 'series', 'base-game', 'derived-games', 'romhacks', 'leaderboard']
        for link_type in range(len(link_types)-1):
            self.final_links.append(self.game_data['links'][link_type]['uri'])
        return self.final_links

    def __init__(self, game = str('')):
        self.game = game