Translation
===
Speedrun.com's api provides ids instead of the name of the thing you are searching for.
The translations module allows you to translate the ids into names you can read.
The translations module also works backworks by translating some names into ids (Sadly not fully supported yet).
This modlue should be built into the code but in the rare chance that it isnt it can be used by the user aswell.
<br>
To use this module you first need to import it.
```python
>>> import speedrunapi.translation as tr
```
Then you can use the tr. or what ever you call it as to call some of the funtions avalible.
```python
>>> region_translated = tr.translate_region("e6lxy1dz")
>>> print(region_translated)
EUR / PAL
```
This is now also fully implemented into the library so code like this wont print the id, but instead will print the region.
```python
>>> from speedrunapi import Game
>>> game = Game("sms")
>>> print(game.regions)
['EUR / PAL']
```
Instead of.
```
>>> print(game.regions)
e6lxy1dz
```
Currently Supported Operations:
===
## Name To ID
- username_to_id: returns a username converted to an id as a string.
- game_name_to_id: returns a game name converted to an id as a string.
## Users
- translate_user_id: Returns the name of a user from a user id
## Games
- translate_game_id: Returns the name of a game from a game id.
- translate_game_abbreviation: Retruns the name of a game from a abbreviation.
## Levels
- translate_level_id: Returns the name of a level from a level id.

## Categories
- translate_category_id: Returns the name of a category from a category id.