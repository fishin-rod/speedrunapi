Speedrun APIS Documentation
===
### A python library to work with the speedrun.com API
### Version = 0.3.1

Usage
===
## Instilation:
```python
>>> pip install speedrunapi
```
Imports the library using pip, currently pip is the only available way to download this library.
## Setup:
```python
>>> import speedrunapi as sr
>>> user = sr.User(username)
>>> game = sr.game(gamename)
```
This imports the speedrunapi library as sr for ease of use, then defines two objects, a game object and a user object. Each object takes 1 parameter a user name, and a game name respectively.
## Getting User Data:
```python
>>> print(user.lookup)
```
This returns a dictionary of all the information on the user provided by Speedrun.com. **(A lot of data)**

## Getting User ID: 
```python
>>> print(user.id)
'jonryvl8'
```
This retrives the id of the user provided in the setup stage. For this example I used my own id.

## Getting Game Data:
```python
>>> print(game.lookup)
```
This returns a diconary of all the data provided by speedrun.com. **(A lot of data)**
## Getting Game ID:
```python
>>>print(game.id)
'j1npme6p'
```
In this example I use the ID of Minecraft: Java Edition.

Currently supported methods:
===
## User
- lookup: Returns the profile data of the user in a dictionary format
- id: Rreturns the ID of the user as a string
- name_style: Returns the name style a user has on speedrun.com as a dictonary
- role: Returns the role of the user as a string
- signup: Returns the join date of the user as a string in the format Y/M/D H/M/S
- location: Returns the location of the user as a dictionary containing information about the country and region
- links: Returns the links the user has listed on their profiles as a list (can be None)
- runs: Returns the runs the user has submitted in a dictionary format
- moderated_games: Returns the games the user moderates as a dictionary
- personal_bests: Returns the personal bests of the user in a dictionary format
## Game
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

## Known Issues
- No currently known issues

## TODO
- Categories (started)
- Guests
- Leaderboards (started)
- Notifications
- Profile
- Errors (started)
- Translation for the ids

### If you have any questions or suggestions please feel free to contact me about them, for issues please report them on the project repository