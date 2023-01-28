from speedrunapi import Game
from speedrunapi.errors import DataFetchError

class Categories:
    
    @property
    def categories(self):
        return self.game_category_data
    
    def game_categories_data(self, keys):
        final_data = []
        for data in range(len(self.game_category_data)):
            final_data.append(self.game_category_data[data][keys])
        return final_data
    
    @property
    def category_ids(self):
        return self.game_categories_data("id")
    
    @property
    def category_names(self):
        return self.game_categories_data("name")
    
    @property
    def category_types(self):
        return self.game_categories_data("type")
    
    @property
    def category_rules(self):
        final_rules = []
        rules = self.game_categories_data("rules")
        for rule in range(len(rules)):
            final_rules.append(rules[rule].replace('\n','').replace('\r',''))
        return final_rules
    
    @property
    def category_players(self):
        return self.game_categories_data("players")
    
    @property
    def category_urls(self):
        final_urls = []
        urls = ['variables', 'records', 'runs', 'leaderboard']
        data = self.game_categories_data("links")
        try:
            for url in range(len(urls)):
                final_urls.append(data[url][url]['uri'])
            return final_urls
        except IndexError:
            raise DataFetchError(f"Incomplete URl set for this category. \nUrls found:{final_urls}")

    def __init__(self, game):
        self.game = game
        self.game_data = Game(self.game)
        self.game_category_data = self.game_data.catagories
        