from speedrunapi import Misc_Requests
from speedrunapi.errors import Region_Length_Error, InvalidRegionError
from speedrunapi.translation import * 
from datetime import datetime
import urllib.error

class Regions:
    """Data about regions on speedrun.com
    ARGS: region, the region id or name of a region on speedrun.com"""
    
    @property
    def region_game(self) -> dict:
        """Gets all the data about games inside the region"""
        try:
            link = Misc_Requests.region_link_request(self.region[0], 1)
        except TypeError:
            link = Misc_Requests.region_link_request(self.region[0][0], 1)
        except urllib.error.HTTPError:
            raise InvalidRegionError(f'"{self.region[0]}" The region provided is not a valid region, check your spelling.')
        return Misc_Requests.region_data_request(link)
    
    @property
    def region_game_names(self) -> list:
        """Returns a list of the names of the games that are included in the region"""
        final_game_names = []
        for id in range(len(self.region_runs)):
            final_game_names.append(self.region_game[id]['names']['international'])
        return final_game_names
    
    @property
    def region_runs(self) -> dict:
        """Returns all of the information avalible for runs in a region"""
        try:
            link = Misc_Requests.region_link_request(self.region[0], 2)
        except TypeError:
            link = Misc_Requests.region_link_request(self.region[0][0], 2)
        except urllib.error.HTTPError:
            raise InvalidRegionError(f'"{self.region[0]}" The region provided is not a valid region, check your spelling.')
        return Misc_Requests.region_data_request(link)
    
    @property
    def region_run_ids(self):
        final_runs_ids = []
        for id in range(len(self.region_runs)):
            final_runs_ids.append(self.region_runs[id]['id'])
        return final_runs_ids
    
    @property
    def region_run_games(self):
        final_games = []
        for id in range(len(self.region_runs)):
            game_id = self.region_runs[id]['game']
            final_games.append(translate_game_id(game_id))
        return final_games
    
    @property
    def region_run_levels(self):
        final_levels = []
        for id in range(len(self.region_runs)):
                level = self.region_runs[id]['level']
                final_levels.append(translate_level(level))
        return final_levels
    
    @property
    def region_run_categories(self):
        final_categories = []
        for id in range(len(self.region_runs)):
                catagory = self.region_runs[id]['category']
                final_categories.append(translate_catagory(catagory))
        return final_categories
    
    @property
    def region_run_status(self):
        final_status = []
        for id in range(len(self.region_runs)):
            status = self.region_runs[id]['status']
            status['examiner'] = translate_user_id(status['examiner'])
            if status['status'] == 'rejected':
                pass
            elif status['verify-date']:
                date_formatted = datetime.fromisoformat(status['verify-date'])
                status['verify-date'] = date_formatted.strftime("%Y-%m-%d %H:%M:%S")
            final_status.append(status)
        return final_status
    
    @property
    def region_run_comments(self):
        final_comments = []
        for id in range(len(self.region_runs)):
            comment = self.region_runs[id]['comment']
            if str(comment).__contains__('\n') or str(comment).__contains__('\r'):
                comment = comment.replace('\n','').replace('\r','')
            final_comments.append(comment)
        return final_comments
    
    @property
    def region_run_users(self):
        final_users = []
        for id in range(len(self.region_runs)):
            user = self.region_runs[id]['players']
            if user[0]['rel'] == 'guest':
                user = user[0]['name']
            else:
                user = translate_user_id(user[0]['id'])
            final_users.append(user)
        return final_users
    
    @property
    def region_run_submitted_dates(self):
        final_date = []
        for id in range(len(self.region_runs)):
            date = self.region_runs[id]['date']
            date_formatted = datetime.fromisoformat(date)
            final_date.append(date_formatted.strftime("%Y-%m-%d"))
        return final_date
    
    @property
    def region_run_times(self):
        run_times = []
        for time in range(len(self.region_runs)):
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
        return run_times
    
    @property
    def region_run_platforms(self):
        final_platforms = []
        for id in range(len(self.region_runs)):
            platform = self.region_runs[id]['system']['platform']
            final_platforms.append(translate_platform(platform))
        return final_platforms

    def __init__(self, *region):
        if len(region) >= 2:
            raise Region_Length_Error("Please only provide one region")
        if len(region[0]) == 0:
            raise Region_Length_Error("Please provide at least one region")
        self.region = region
