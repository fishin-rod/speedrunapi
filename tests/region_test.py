from speedrunapi import Regions
from speedrunapi import Game
import time

start = time.time()

game = Game('sms') 
region = game.regions

region = 'e6lxy1dz'

re = Regions(region)

def region_games(re):
    print(re.region_game)
    print(re.region_game_names)

def region_runs(re):
    print(re.region_runs)
    print(re.region_run_ids)
    print(re.region_run_games)
    print(re.region_run_levels)
    print(re.region_run_categories)
    print(re.region_run_status)
    print(re.region_run_comments)
    print(re.region_run_users)
    print(re.region_run_submitted_dates)
    print(re.region_run_times)
    print(re.region_run_platforms)

region_games(re)
region_runs(re)

end = time.time()

print(end - start)
