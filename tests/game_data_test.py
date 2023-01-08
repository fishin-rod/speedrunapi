from speedrunapi import Game
import time

start = time.time()

def main_functions(game):
    print(game.lookup)
    print(game.format_name)
    print(game.id)
    print(game.abbreviation)
    print(game.realease_date)
    print(game.ruleset)
    print(game.regions)
    print(game.platforms)
    print(game.genres)
    print(game.engines)
    print(game.admins)
    print(game.join_date)

def special_cases(game):
    print(game.levels)
    print(game.catagories)
    print(game.variables)
    print(game.records)
    print(game.series)
    print(game.derived_games)
    print(game.romhacks)
    print(game.leaderboard)

game = Game('Minecraft: Java Edition')
main_functions(game)
special_cases(game)

end = time.time()
print(end - start)
print(game.lookup)
