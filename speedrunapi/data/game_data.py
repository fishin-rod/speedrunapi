from speedrunapi import Game_Requests
from datetime import datetime

class Game:
    """Data about a game on speedrun.com
    ARGS: game, the full name of the game on speedrun.com"""
    
    @property
    def lookup(self):
        """Retruns the full game data from speedrun.com as a dictionary"""
        return self.game_data.game_data
    
    @property
    def format_name(self):
        """Returns the name of the game on speedrun.com but formated so it can be used in links as a string"""
        self.formated_game_name = ''
        for i in range(len(self.game)):
            if self.game[i] == ' ':
                self.formated_game_name = self.formated_game_name + "%20"
            else:
                self.formated_game_name = self.formated_game_name + self.game[i]
        return self.formated_game_name
    
    @property 
    def id(self):
        """Returns the id of the game on speedrun.com as a string"""
        self.game_id = self.quick_game_data.quick_game_data['data'][0]['id']
        return self.game_id
    
    @property
    def abbreviation(self):
        """Returns the abbreviaion of the name of a game on speedrun.com as a string"""
        return self.game_data.game_data['abbreviation']
    
    @property
    def realease_date(self):
        """Returns the data a game was realeased to the public as listed on speedrun.com in a string"""
        return self.game_data.game_data['release-date']
    
    @property
    def ruleset(self):
        """Returns the ruleset of a game on speedrun.com as a dictionary"""
        return self.game_data.game_data['ruleset']
    
    @property
    def regions(self):
        """Returns the regions of a game on speedrun.com as a dictionary 
        (wont look like a real region(soon to add a way to translate these))"""
        return self.game_data.game_data['regions']
    
    @property
    def platforms(self):
        """Returns the platforms of a game on speedrun.com as a dictionary 
        (wont look like a real platform(soon to add a way to translate these))"""
        return self.game_data.game_data['platforms']
    
    @property
    def genres(self):
        """Returns the genres of a game on speedrun.com as a dictionary 
        (wont look like a real genre(soon to add a way to translate these))"""
        return self.game_data.game_data['genres']
    
    @property
    def engines(self):
        """Returns the engines of a game on speedrun.com as a dictionary 
        (wont look like a real engine(soon to add a way to translate these))"""
        return self.game_data.game_data['engines']
    
    @property
    def admins(self):
        """Returns the developers,publishers, and moderators of a game on speedrun.com as a dictionary"""
        final_admins = []
        admin_list = ['developers', 'publishers', 'moderators']
        for admin in admin_list:
            admins = self.game_data.game_data.get(admin, [])
            final_admins.append(admins)
        return final_admins
    
    @property
    def join_date(self):
        """Returns the data a game joined speedrun.com as a string"""
        date_unformatted = self.game_data.game_data['created']
        date_formatted = datetime.fromisoformat(date_unformatted)
        return date_formatted.strftime('%Y-%m-%d')
    
    #special cases
    @property
    def runs(self):
        """Returns the runs of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(1)
        return self.game_data.game_data_response

    @property
    def levels(self):
        """Returns the levels of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(2)
        return self.game_data.game_data_response
    
    @property
    def catagories(self):
        """Returns the catagories of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(3)
        return self.game_data.game_data_response
    
    @property
    def variables(self):
        """Returns the variables of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(4)
        return self.game_data.game_data_response
    
    @property
    def records(self):
        """Returns the records of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(5)
        return self.game_data.game_data_response

    @property
    def series(self):
        """Returns the series of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(6)
        return self.game_data.game_data_response
    
    @property
    def derived_games(self):
        """Returns the derived games of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(7)
        return self.game_data.game_data_response
    
    @property
    def romhacks(self):
        """DEPRICATED returns the same as derived games, here for backwards compatiblilty
        Returns the romhacks of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(8)
        return self.game_data.game_data_response
    
    @property
    def leaderboard(self):
        """Returns the leaderboard of a game on speedrun.com as a dictionary"""
        self.game_data.game_data_request(9)
        return self.game_data.game_data_response
    
    def __init__(self, game = str('')):
        self.game = game
        self.format_name
        self.quick_game_data = Game_Requests(self.formated_game_name)
        self.quick_game_data.game_reqest_quick()
        self.game_id = self.id
        self.game_data = Game_Requests(self.id)
        self.game_data.game_request()   