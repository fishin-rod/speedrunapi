from speedrunapi import Game, Game_Requests

class Levels:
    
    def game_levels_data(self, keys):
        self.final_level_data = []
        for level in range(0, 100000):
            try:
                self.final_level_data.append(self.game_level_data[level][keys])# type: ignore            
            except IndexError:
                break
        return self.final_level_data

    @property
    def levels(self):
        return self.game_level_data
    
    @property
    def level_ids(self):
        return self.game_levels_data("id")
    
    @property
    def level_names(self):
        return self.game_levels_data("name")
    
    @property
    def level_rules(self):
        return self.game_levels_data("rules")
    
    def __init__(self, game):
        self.game = game
        self.game_data = Game(self.game)
        self.game_id = self.game_data.id
        self.game_data = Game_Requests(self.game_id)
        self.game_data.game_request()
        self.game_level_data = self.game_data.game_data_request(2)
