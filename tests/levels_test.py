from speedrunapi import Levels
import time

start = time.time()
def levels(game):
    print(level.levels)
    print(level.level_ids)
    print(level.level_names)
    print(level.level_rules)

level = Levels('sm64')
levels(level)
end = time.time()
print(end - start)