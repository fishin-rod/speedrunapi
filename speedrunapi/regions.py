from speedrunapi import Misc_Requests
from speedrunapi.errors import Region_Length_Error
from speedrunapi.translation import * 
from datetime import datetime

class Regions:
    """Data about regions on speedrun.com
    ARGS: region, the region id or name of a region on speedrun.com"""
    
    @property
    def region_game(self):
        """Gets all the data about games inside the region"""
        try:
            link = Misc_Requests.region_link_request(self.region[0], 1)
        except TypeError:
            link = Misc_Requests.region_link_request(self.region[0][0], 1)
        return Misc_Requests.region_data_request(link)
    
    @property
    def region_game_names(self):
        """Returns a list of the names of the games that are included in the region"""
        final_game_names = []
        for id in range(0,100000):
            try:
                final_game_names.append(self.region_game[id]['names']['international'])
            except IndexError:
                break
        return final_game_names
    
    @property
    def region_runs(self):
        """Returns all of the information avalible for runs in a region"""
        try:
            link = Misc_Requests.region_link_request(self.region[0], 2)
        except TypeError:
            link = Misc_Requests.region_link_request(self.region[0][0], 2)
        return Misc_Requests.region_data_request(link)
    
    @property
    def region_run_ids(self):
        final_runs_ids = []
        for id in range(0,100000):
            try:
                final_runs_ids.append(self.region_runs[id]['id'])
            except IndexError:
                break
        return final_runs_ids
    
    @property
    def region_run_games(self):
        final_games = []
        for id in range(0,100000):
            try:
                game_id = self.region_runs[id]['game']
                final_games.append(translate_game_id(game_id))
            except IndexError:
                break
        return final_games
    
    @property
    def region_run_levels(self):
        final_levels = []
        for id in range(0,100000):
            try:
                level = self.region_runs[id]['level']
                final_levels.append(translate_level(level))
            except IndexError:
                break
        return final_levels
    
    @property
    def region_run_categories(self):
        final_categories = []
        for id in range(0,100000):
            try:
                catagory = self.region_runs[id]['category']
                final_categories.append(translate_catagory(catagory))
            except IndexError:
                break
        return final_categories
    
    @property
    def region_run_status(self):
        final_status = []
        for id in range(0,100000):
            try:
                status = self.region_runs[id]['status']
                status['examiner'] = translate_user_id(status['examiner'])
                if status['status'] == 'rejected':
                    pass
                elif status['verify-date']:
                    date_formatted = datetime.fromisoformat(status['verify-date'])
                    status['verify-date'] = date_formatted.strftime("%Y-%m-%d %H:%M:%S")
                final_status.append(status)
            except IndexError:
                break
        return final_status
    
    @property
    def region_run_comments(self):
        final_comments = []
        for id in range(0,100000):
            try:
                comment = self.region_runs[id]['comment']
                if str(comment).__contains__('\n') or str(comment).__contains__('\r'):
                    comment = comment.replace('\n','').replace('\r','')
                final_comments.append(comment)
            except IndexError:
                break
        return final_comments
    
    @property
    def region_run_users(self):
        final_users = []
        for id in range(0,100000):
            try:
                user = self.region_runs[id]['players']
                if user[0]['rel'] == 'guest':
                    user = user[0]['name']
                else:
                    user = translate_user_id(user[0]['id'])
                final_users.append(user)
            except IndexError:
                break
        return final_users
    
    @property
    def region_run_submitted_dates(self):
        final_date = []
        for id in range(0,100000):
            try:
                date = self.region_runs[id]['date']
                date_formatted = datetime.fromisoformat(date)
                final_date.append(date_formatted.strftime("%Y-%m-%d"))
            except IndexError:
                break
        return final_date
    
    @property
    def region_run_times(self):
        run_times = []
        for time in range(0, 100000):
            try:
                unformatted_date = self.region_runs[time]["times"]["primary_t"]
                if unformatted_date / 60 < 1:
                    seconds = "S:", unformatted_date
                    run_times.append(seconds)
                elif unformatted_date / 3600 < 1:
                    minutes = "M:", round(unformatted_date / 60, 2)
                    run_times.append(minutes)
                else:
                    hours = "H:", round(unformatted_date / 3600, 2)
                    run_times.append(hours)
            except IndexError:
                break
        return run_times
    
    @property
    def region_run_platforms(self):
        final_platforms = []
        for id in range(0,100000):
            try:
                platform = self.region_runs[id]['system']['platform']
                final_platforms.append(translate_platform(platform))
            except IndexError:
                break
        return final_platforms

    def __init__(self, *region):
        if len(region) >= 2:
            raise Region_Length_Error("Please only provide one region")
        if len(region[0]) == 0:
            raise Region_Length_Error("Please provide at least one region")
        self.region = region
