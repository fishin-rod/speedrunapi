from speedrunapi import Misc_Requests
from speedrunapi.errors import DataFetchError
from speedrunapi.translation import *
from datetime import datetime
import asyncio
from aiohttp import ClientSession
from functools import lru_cache

class Leaderboard:
    @lru_cache(maxsize=100)
    async def translate_user_id(self,):  # this allows for large data requests to be made faster internaly for the library for matters like translation
        async with ClientSession() as session:
            self.names = []
            for name in self.run_users:
                try:
                    url = f"https://www.speedrun.com/api/v1/users/{name}"
                    async with session.get(url) as resp:
                        name = await resp.json()
                        self.names.append(name["data"]["names"]["international"])
                except KeyError:
                    pass
            return self.names

    @property
    def leaderboard(self):
        """All the data for a leaderboard on speedrun.com"""
        return self.leaderboard_data

    @property
    def leaderboard_top(self):
        """Returns the leaderboard with the person and place (can cause lots of lag)
        Takes in the argument of the top amount of places you want (defaults to 50000 or whatever the max is)"""
        final_places = []
        if self.limit is None:
            self.limit = 50000
        for place in range(0, self.limit):
            try:
                place = self.leaderboard_data["runs"][place]["place"]
                if self.leaderboard_data["runs"][place]["run"]["players"][0]["rel"] == "guest":
                    final_places.append(None)
                name = self.leaderboard_data["runs"][place]["run"]["players"][0]["id"]
                final_places.append(str(place) + " : " + str(translate_user_id(name)))
            except KeyError:
                final_places.append(None)
            except IndexError:
                break
        return final_places

    @property
    def leaderboard_run_ids(self):
        """Returns a list of the ids repersenting each indivdual run for the leaderboard"""
        if self.limit is None:
            self.limit = len(self.leaderboard_data["runs"])
        run_ids = []
        for run_id in range(0, self.limit):
            try:
                run_ids.append(self.leaderboard_data["runs"][run_id]["run"]["id"])
            except IndexError:
                break
        return run_ids

    @property
    def leaderboard_run_comments(self):
        """Returns a list of the comments for each of the runs on the leaderboard"""
        if self.limit is None:
            self.limit = len(self.leaderboard_data["runs"])
        run_comments = []
        for run_id in range(0, self.limit):
            try:
                comment = self.leaderboard_data["runs"][run_id]["run"]["comment"]
                if str(comment).__contains__("\n") or str(comment).__contains__("\r"):
                    comment = comment.replace("\n", "").replace("\r", "")
                run_comments.append(comment)
            except IndexError:
                break
        return run_comments

    @property
    def leaderboard_run_status(self) -> list:
        """Returns a list of the status of runs.
        The values you will see in each list index are:
        status: verified - meaning that the run is verified to be not cheated,
        examiner: (name) - the name of the person that verified the run,
        verify-date: (date) - the date the run was verified."""
        if self.limit is None:
            self.limit = len(self.leaderboard_data["runs"])
        run_status = []
        for run_id in range(0, self.limit):
            try:
                status = self.leaderboard_data["runs"][run_id]["run"]["status"]
                status["examiner"] = translate_user_id(status["examiner"])
                if status["status"] == "rejected":
                    pass
                elif status["verify-date"]:
                    date_formatted = datetime.fromisoformat(status["verify-date"])
                    status["verify-date"] = date_formatted.strftime("%Y-%m-%d %H:%M:%S")
                run_status.append(status)
            except IndexError:
                break
        return run_status

    def leaderboard_run_users(self, translation=False):
        """Returns the users who have made a run on speedrun.com in order.
        CAN TAKE A LONG TIME DEPENDING ON THE SIZE OF THE LEADERBOARD

        ARGS:
        translation (bool): if True, translate the user_id to their international name,
        if False (default), just return the user_ids for improved performance"""
        if self.limit is None:
            self.limit = len(self.leaderboard_data["runs"])
        self.run_users = []
        for run_id in range(0, self.limit):
            try:
                user = self.leaderboard_data["runs"][run_id]["run"]["players"]
                if user[0]["rel"] == "guest":
                    user = user[0]["name"]
                else:
                    user = user[0]["id"]
                self.run_users.append(user)
            except IndexError:
                break
        if translation:
            people = asyncio.run(self.translate_user_id())
            return people
        else:
            return self.run_users

    @property
    @lru_cache(maxsize=100)
    def leaderboard_run_times(self):
        """Returns a list of the times of each run on the leaderboard in order
        What you should see:
        'H', 'M', or 'S' meaning hours, minutes, or seconds respecivly.
        A float with two decimal places repersenting the time.

        Examples:
        - ('H': 2.42) repersenting a time of 2 hours and 42 minutes.
        - ('M': 2.42) repersenting a time of 2 minutes and 42 seconds.
        - ('S': 2.42) repersenting a time of 2 seconds and 42 miliseconds."""
        if self.limit is None:
            self.limit = len(self.leaderboard_data["runs"])
        run_times = []
        for run_time in range(0, self.limit):
            try:
                unformatted_date = self.leaderboard_data["runs"][run_time]["run"]["times"]["primary_t"]
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
    @lru_cache(maxsize=100)
    def leaderboard_run_platforms(self):
        """Returns a list of the platforms used for each of the runs in order."""
        if self.limit is None:
            self.limit = len(self.leaderboard_data["runs"])
        run_platforms = []
        for run_platform in range(0, self.limit):
            try:
                platform = self.leaderboard_data["runs"][run_platform]["run"]["system"]["platform"]
                run_platforms.append(translate_platform(platform))
            except IndexError:
                break
        return run_platforms

    @property
    @lru_cache(maxsize=100)
    def leaderboard_run_regions(self):
        """Returns a list of the regions each of the runs was  in."""
        if self.limit is None:
            self.limit = len(self.leaderboard_data["runs"])
        run_regions = []
        for run_region in range(0, self.limit):
            try:
                region = self.leaderboard_data["runs"][run_region]["run"]["system"]["region"]
                if region:
                    run_regions.append(translate_region(region))
                else:
                    run_regions.append(region)
            except IndexError:
                break
        return run_regions

    # TODO ADD TRANSLATION FOR RUN VALUES AND FIGURE OUT WHAT THEY ARE

    def __init__(self, game, category=None, limit=None):
        """LEADERBOARD data from the speedrun.com API

        Args:
            game (str): The name of the game you want to get the leaderboard for
            category (str, optional): The category you want to get the leaderboard for.
        If not provided will take the defult one from speedrun.com
            limit (int, optional): The amount of runs you want to have returned
        Defaults to the maximum amount"""
        from speedrunapi import Categories

        self.limit = limit
        # checks to see if you have provided the category, if you have not then it takes the default
        if category:
            url = f"https://www.speedrun.com/api/v1/leaderboards/{game_name_to_id(game)}/category/{category_name_to_id(game, category)}"
        else:
            category = Categories(game)
            try:
                url = category.category_urls[3]
            except DataFetchError:
                url = category.final_urls[0]
                url += "/records"
        self.leaderboard_data = Misc_Requests.leaderboard_data_request(url)
