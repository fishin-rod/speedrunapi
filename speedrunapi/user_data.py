from speedrunapi import User_Requests
from datetime import datetime
import http.client
from .errors import URLerror

class User:
    """Data about a user on speedrun.com
    ARGS: user, a username of a person on speedrun.com"""

    @property
    def lookup(self):
        """Returns the users full_data on speedrun.com"""
        return self.user_data.user_data

    @property
    def id(self):
        """Returns the id of the user as a string"""
        userid = [id.get("id") for id in self.user_data.user_data]
        return userid[0]

    @property
    def name_style(self):
        """Returns the name style of the user as a dictionary"""
        return self.user_data.user_data[0]["name-style"]

    @property
    def role(self):
        """Returns the speedrun.com role of the user as a string"""
        return self.user_data.user_data[0]["role"]

    @property
    def signup(self):
        """Returns the date the user joined speedrun.com as a string in the format Y-M-D H:M:S"""
        date_unformatted = self.user_data.user_data[0]["signup"]
        date_formatted = datetime.fromisoformat(date_unformatted)
        return date_formatted.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def location(self):
        """Returns the location the user has listed on speedrun.com as a dictionary"""
        return self.user_data.user_data[0]["location"]

    @property
    def links(self):
        """Returns the links the user has listed on their profile on speedrun.com as a list"""
        final_links = []
        link_types = ["twitch", "hitbox", "youtube", "twitter", "speedunslive"]
        for link_type in range(len(link_types)):
            final_links.append([link.get(link_types[link_type]) for link in self.user_data.user_data])
        return final_links

    # special cases

    @property
    def moderated_games(self):
        """Returns a dictionary of all the moderated games a user has on speedrun.com"""
        self.user_data.user_data_request(2)
        moderated = self.user_data.user_data_response
        if len(moderated) == 0:
            return "User moderates no games"
        else:
            return moderated

    @property
    def personal_bests(self):
        """Returns a dictionary of the personal bests of a user on speedrun.com"""
        self.user_data.user_data_request(3)
        return self.user_data.user_data_response

    def __init__(self, user):
        try:
            self.user = user
            self.user_data = User_Requests(self.user)
        except http.client.InvalidURL as e:
            details = e.args[0].split("'")[2]
            raise URLerror(f'{details}\nCheck to make sure the name acctualy has no alphanumeric characters/spaces')
