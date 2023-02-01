Leaderboard
===

On speedrn.com each game has a leaderboard for each of is categories.

To use the leaderboard function from the library you have to provide 1 to 3 parameters.

```python
>>> from speedrunapi import Leaderboard

>>> l = Leaderboard("Minecraft: Java Edition", "Any%", 10)
```
The first parmater is the game witch is required, the second parameter is the category witch is optional(defults to the category provided in the url), and lasty the thrid parameter is the number of places you want to see(defults to he maximum).

Now that you have a leaderboard object set up you can start the operations.
```python
>>> print(l.leaderboard)
```
Returns the leaderboard data for the game/category
