Games
===
Speedrun.com allows you to query for game data, the game class allows you to get this data using this library.
<br>
To initialize a game object you use the following code replacing Minecraft: Java Edition with the name of the game you are looking for, and replacing game with the variable name you want associated with the game inputed. 
<br>
The class takes one parameter, the name of a game stored as a string in a variable or a string, 0 or 2+ parameters entered will give a type error.
```python
game = speedrunapi.Game('Minecraft: Java Edition')
```
Great! You have set up a game object, now its time to do operations on that game object.
<br>
To do opperations on a game, just add one of the supported operations to the game object.
<br>
If you do the opperation id to the game it will return the id of the game put into the program.
```python
>>> print(game.id)
j1npme6p
```
Or you can do it directly to the game object.
```python
>>> print(speedrunapi.Game('Minecraft: Java Edition').id)
j1npme6p
```
Currently supported operations:
===
- lookup: Returns the game data of the game as a dictionary
- format_name: Returns the games name but formated to be used in the links as a string
- id: Returns the id of the game as a string
- abbreviation: Returns the abbreviation of the game as a string
- release_date: Returns the release date of the game as a string
- ruleset: Returns the ruleset of the game as dictionary
- regions: Returns the region ids of the game as a dictionary (can be [])
- platforms: Returns the platform ids of the game as a dictionary (can be [])
- genres: Returns the genre ids of the game as a dictionary (can be [])
- engines: Returns the engin ids of the game as a dictionary (can be [])
- admins: Returns the developers, publishers, and moderators of the game as a dictionary
- join_date: Returns the date the game joined speedrun.com as a string
- runs: Returns the runs of the game as a dictionary
- levels: Returns the leves of a game as a dictionary
- categories: Returns the categories of the game as a dictionary
- variables: Returns the variables of the game as a dictionary
- records: Returns the records of the game as a dictionary
- series: Returns the series of the game as a dictionary
- derived_games: Returns the derived games of the game as a dictionary
- romhacks: LEGACY VALUE! user derived_games insted, its here just for backwards compatibility
- leaderboard: Returns the leaderboard of the game for a category as a dictionary (currently adding support for different categories)
