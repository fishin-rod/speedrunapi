Runs
===
There are two distinct catagories for runs on speedrun.com **Users** and **Games**.
<br>
*NOTE: A lot of the information in this document is very similar to [users](user.md) and [games](game.md).*
<br>
<br>
User runs are runs made by one single user across many games.
<br>
Game Runs are made by many users in a single game across lots of different catagories. Currently Game runs can only be in one catagory but I plan to add support for multiple catagories.
<br>
To setup a user run class first import the library and define a user. 
```python
>>> import speedrunapi
>>> user = speedrunapi.User_Runs("fishin_rod")
```
Next you can do operations on the user you just provided.
```python
>>>print(user.runs)
```
This will output a lot of data about a users runs. To access more specific data use some of the other operations.
```python
>>>print(user.run_submitted_dates)
['2022-12-21 18:47:39', '2022-12-21 00:44:13', '2022-12-21 14:45:21', '2022-12-21 18:19:44', '2022-12-21 18:31:10']
```
Currnetly Supported Operations
===
## User
- runs: Returns a dictionary of all the information avalible about the users runs.
- run_ids: Returns a list of all of the unique ids that are linked to runs the user has.
- run_games: Returns a list of the ids of games that the user has submitted runs for.
- run_catagories: Returns a list of the ids of catagoies that the user has submitted runs for.
- run_videos: Returns a list of links for the video provided for runs by the user.
- run_comments: Returns a list of comments for runs by the user.
- run_status: Returns the status of runs by the user.
- run_examiners: Returns a list of ids of users who have examined runs by the user.
- run_verify_dates: Returns the dates when a run by the user was verified.
- run_submitted_dates: Returns a list of dates of when a user submitted runs.

## Game
- runs: Returns a dictionary of all the information avalible about the games runs.
- run_ids: Returns a list of all of the unique ids that are linked to runs the game has.
- run_levels: Returns a list of the ids of levels that the game has runs for.
- run_catagories: Returns a list of the ids of catagoies that the game has runs for.(should all be the same since all the runs are for a given catagory).
- run_videos: Returns a list of links for the video provided for runs.
- run_comments: Returns a list of comments for runs.
- run_status: Returns the status of runs.
- run_examiners: Returns a list of ids of users who have examined runs for the game.
- run_verify_dates: Returns the dates when a run by a user was verified.
- run_users: Returns a list of ids of users who have submitted runs for the game.
- run_submitted_dates: Returns a list of dates of when a run by a use was submitted runs.
- run_times: Returns a list of the ingame times for runs
- run_platforms: Returns a list of the platfroms that a game has been run on.
- run_values: Returns a list of the values assosiated with the game.