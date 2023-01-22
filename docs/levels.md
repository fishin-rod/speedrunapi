Levels
===
Levels are subcatagories of games, not all games will have levels
<br>
After importing the library you can start to use the library
```python
>>> level = speedrunapi.Level("sm64")
>>> print(level.level_names)
['Maple Meadow', 'Polar Peaks', 'Lush Lagoon', 'Torchlight Temple', 'Supersonic Slide', 'Bowser in the Gloomy Sea']
```
This prints the names of the levels in the library.

Currently Supported Operations
===
- levels: Returns all the data about levels avalible for the game.
- level_ids: Returns all the level ids for levels in the game.
- level_names: Returns all the names of levels in the game.
- level_rules: Returns the rules for each level of a game.