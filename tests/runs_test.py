from speedrunapi import Game_Runs, User_Runs
import time

start = time.time()

def user_runs(user):
    print(user.runs)
    print(user.run_ids)
    print(user.run_games)
    print(user.run_catagories)
    print(user.run_videos)
    print(user.run_comments)
    print(user.run_status)
    print(user.run_examiners)
    print(user.run_verify_dates)
    print(user.run_submitted_dates)

def game_runs(game):
    print(game.runs)
    print(game.run_ids)
    print(game.run_levels)
    print(game.run_catagories)
    print(game.run_videos)
    print(game.run_comments)
    print(game.run_status)
    print(game.run_examiners)
    print(game.run_verify_dates)
    print(game.run_users)
    print(game.run_submitted_dates)
    print(game.run_times)
    print(game.run_platforms)
    print(game.run_values)

game = Game_Runs('Minecraft: Java Edition')
user = User_Runs('fishin_rod')
user_runs(user)
game_runs(game)

end = time.time()
print(end-start)
