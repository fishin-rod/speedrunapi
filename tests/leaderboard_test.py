from speedrunapi import Leaderboard
import time

start = time.time()

l = Leaderboard('Minecraft: Java Edition', 'Any%', 100)

print(l.leaderboard)
print(l.leaderboard_top)
print(l.leaderboard_run_ids)
print(l.leaderboard_run_comments)
print(l.leaderboard_run_status)
print(l.leaderboard_run_users(False)) #can also be true
print(l.leaderboard_run_times)
print(l.leaderboard_run_platforms)
print(l.leaderboard_run_regions)

end = time.time()
print(end-start)