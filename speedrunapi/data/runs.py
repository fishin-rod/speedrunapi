from speedrunapi import User_Requests
from speedrunapi import Game_Requests
from speedrunapi import Game
from datetime import datetime
#add a way to set the catagories for game runs

class User_Runs:
    """Data about a users runs on speedrun.com
    ARGS: User, the user you want to get the runs for"""

    @property
    def runs(self):
        """Returns a dictionary of all the runs a user has on speedrun.com"""
        return self.user_run_data

    def user_runs_data(self,keys):
        final_run_data = []
        for run in range(0,100000):
            try:
                final_run_data.append(self.user_run_data[run][keys])
            except IndexError:
                break
        return final_run_data
    
    @property
    def run_ids(self):
        """Returns a list of all the ids of runs a user has on speedrun.com"""
        return self.user_runs_data('id')
    
    @property
    def run_games(self):
        """Returns a list of all of the games a user has run on speedrun.com"""
        return self.user_runs_data('game')

    @property
    def run_levels(self):
        """Returns a list of all of the levels a user has run on speedrun.com"""
        return self.user_runs_data('level')
    
    @property
    def run_catagories(self):
        """Returns a list of all of the catagories a user has run on speedrun.com"""
        return self.user_runs_data('category')
    
    @property
    def run_videos(self):
        """Returns a list of all of the videos a user has for runs on speedrun.com"""
        videos = []
        for video in range(0,100000):
            try:
                videos.append(self.user_run_data[video]['videos']['links'][0]['uri'])
            except IndexError:
                break
        return videos
  
    @property
    def run_comments(self):
        """Returns a list of all of the comments a user has for runs on speedrun.com"""
        return self.user_runs_data('comment')

    @property
    def run_status(self):
        """Returns a list of the status of a users runs on speedrun.com"""
        status = []
        for stat in range(0,100000):
            try:
                status.append(self.user_run_data[stat]['status']['status'])
            except IndexError:
                break
        return status

    @property
    def run_examiners(self):
        """Returns a list of the users who have examined a users runs on speedrun.com"""
        examiners = []
        for examiner in range(0,100000):
            try:
                examiners.append(self.user_run_data[examiner]['status']['examiner'])
            except IndexError:
                break
        return examiners
    
    @property
    def run_verify_dates(self):
        """Returns a list of the dates when a users runs were verified on speedrun.com"""
        verify_dates = []
        for verify_date in range(0,100000):
            try:
                unformatted_date =self.user_run_data[verify_date]['status']['verify-date']
                formatted_date =  datetime.fromisoformat(unformatted_date)
                verify_dates.append(formatted_date.strftime("%Y-%m-%d %H:%M:%S"))
            except IndexError:
                break
        return verify_dates
    
    @property
    def run_submitted_dates(self):
        """Returns a list of the dates when a users runs were submitted on speedrun.com"""
        submitted_dates = []
        for submitted_date in range(0,100000):
            try:
                unformatted_date =self.user_run_data[submitted_date]['submitted']
                formatted_date =  datetime.fromisoformat(unformatted_date)
                submitted_dates.append(formatted_date.strftime("%Y-%m-%d %H:%M:%S"))
            except IndexError:
                break
        return submitted_dates

    def __init__(self, user):
        self.user = user
        self.user_data = User_Requests(self.user)
        self.user_run_data = self.user_data.user_data_request(1)['data']

class Game_Runs:
    """Data about a certin games runs on speedrun.com
    ARGS: Game, the game you want to get the runs for. 
    (SOON!) Catagory ID, the ID of the specific catagory you want to get runs for."""

    def game_runs_data(self,keys):
        self.final_run_data = []
        for run in range(0,100000):
            try:
                self.final_run_data.append(self.game_run_data[run][keys])
            except IndexError:
                break
        return self.final_run_data
    
    @property
    def runs(self):
        """Returns a dictionary of all the runs a user has on speedrun.com"""
        return self.game_run_data
    
    @property
    def run_ids(self):
        """Returns a list of all the ids of runs a user has on speedrun.com"""
        return self.game_runs_data('id')
    
    @property
    def run_levels(self):
        """Returns a list of all of the levels a user has run on speedrun.com"""
        return self.game_runs_data('level')
    
    @property
    def run_catagories(self):
        """Returns a list of all of the catagories a user has run on speedrun.com"""
        return self.game_runs_data('category')
    
    @property
    def run_videos(self):
        """Returns a list of all of the videos a game has for runs on speedrun.com"""
        videos = []
        for video in range(0,100000):
            try:
                videos.append(self.game_run_data[video]['videos']['links'][0]['uri'])
            except IndexError:
                break
        return videos
  
    @property
    def run_comments(self):
        """Returns a list of all of the comments a game has for runs on speedrun.com"""
        return self.game_runs_data('comment')

    @property
    def run_status(self):
        """Returns a list of the status of a users runs on speedrun.com"""
        status = []
        for stat in range(0,100000):
            try:
                status.append(self.game_run_data[stat]['status']['status'])
            except IndexError:
                break
        return status

    @property
    def run_examiners(self):
        """Returns a list of the users who have examined a users runs on speedrun.com"""
        examiners = []
        for examiner in range(0,100000):
            try:
                examiners.append(self.game_run_data[examiner]['status']['examiner'])
            except IndexError:
                break
        return examiners
    
    @property
    def run_verify_dates(self):
        """Returns a list of the dates when a users runs were verified on speedrun.com"""
        verify_dates = []
        for verify_date in range(0,100000):
            try:
                unformatted_date =self.game_run_data[verify_date]['status']['verify-date']
                if unformatted_date == None:
                    verify_dates.append(None)
                    continue
                formatted_date =  datetime.fromisoformat(unformatted_date)
                verify_dates.append(formatted_date.strftime("%Y-%m-%d %H:%M:%S"))
            except KeyError:
                break
        return verify_dates
    
    @property
    def run_users(self):
        """Returns a list of the users who have submitted a run on speedrun.com"""
        users = []
        for user in range(0,100000):
            try:
                if self.game_run_data[user]['players'][0]['rel'] == 'guest':
                    users.append(self.game_run_data[user]['players'][0]['name'])
                else:
                    users.append(self.game_run_data[user]['players'][0]['id'])
            except IndexError:
                break
        return users
    
    @property
    def run_submitted_date(self):
        """Returns a list of the dates when a users runs were submitted on speedrun.com"""
        submitted_dates = []
        for submit_date in range(0,100000):
            try:
                unformatted_date =self.game_run_data[submit_date]['submitted']
                if unformatted_date == None:
                    submitted_dates.append(None)
                    continue
                formatted_date =  datetime.fromisoformat(unformatted_date)
                submitted_dates.append(formatted_date.strftime("%Y-%m-%d %H:%M:%S"))
            except IndexError:
                break
        return submitted_dates
    
    @property
    def run_times(self):
        """Returns a list of the times for runs on speedrun.com"""
        run_times = []
        for time in range(0,100000):
            try:
                unformatted_date = self.game_run_data[time]['times']['primary_t']
                if unformatted_date/60 < 1:
                    seconds = 'S:', unformatted_date
                    run_times.append(seconds)
                elif unformatted_date/3600 < 1:
                    minutes = 'M:', round(unformatted_date/60,2)
                    run_times.append(minutes)
                else:
                    hours = 'H:', round(unformatted_date/3600,2)
                    run_times.append(hours)
            except IndexError:
                break
        return run_times
    
    @property
    def run_platforms(self):
        """Returns a list of the platforms for runs on speedrun.com"""
        platforms = []
        for platform in range(0,100000):
            try:
                platforms.append(self.game_run_data[platform]['system']['platform'])
            except IndexError:
                break
        return platforms
    
    @property
    def run_values(self):
        """Returns a list of the values for runs on speedrun.com"""
        values = []
        for value in range(0,100000):
            try:
                values.append(self.game_run_data[value]['values'])
            except IndexError:
                break
        return values

    def __init__(self, game):
        self.game = game
        self.game_data = Game(self.game)
        self.game_id = self.game_data.id
        self.game_data = Game_Requests(self.game_id)
        self.game_data.game_request()
        self.game_run_data = self.game_data.game_data_request(1)
