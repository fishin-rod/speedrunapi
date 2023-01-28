from speedrunapi import Misc_Requests 
#from speedrunapi import Categories
from speedrunapi.errors import DataFetchError
#from speedrunapi.translation import game_name_to_id, category_name_to_id
#how to get category id translated?

class Leaderboard:
    '''
    def __init__(self, game, category = None):
        if category:
            #url = f'https://www.speedrun.com/api/v1/leaderboards/{game_name_to_id(game)}/category/{category_name_to_id(category)}'
            #print(url)
            url = 'f'
        else:
            category = Categories(game)
            try:
                url = category.game_category_urls[3]
            except DataFetchError:
                url = category.final_urls[0]
                url += '/records'
        self.data = Misc_Requests.leaderboard_data_request(url)
            
''' 