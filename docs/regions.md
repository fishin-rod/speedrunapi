Regions
===
A region is the area where a game is published. Not all games have a region listed.

How to use regions:
First you will need to import the library, then you can start.
First you need to get a region.
<br>
Getting a region can be done in two ways, getting the regions directly from the game:
```python
>>> game = Game('sms')
>>> regions = Regions(game.regions)
```
Or you can directly put in the region:
```python
>>> region = Regions('e6lxy1dz')
```
<br>
Once you have a region defined you can start doing operations on it.
```python
>>> print(region.region_games)
["'Allo 'Allo! Cartoon Fun!", "'n Verlore Verstand", "'Splosion Man", '(Mario) The Music Box Remastered', '(The) Final Fantasy Legend', '-SPROUT-', '.hack//G.U. Last Recode', '.hack//Infection', '.hack//Mutation', '.hack//Outbreak', '.hack//Quarantine', '007: Agent Under Fire', '007: From Russia With Love', '007: NightFire (GBA)', '007: Nightfire Category Extensions', '007: The World is Not Enough', '007: The World is Not Enough (PS1)', '10 Second Run Returns', '10-Yard Fight', '100th Anniversary of the Crossword Puzzle']
```

Currently Supported Operations
===
- region_game: Retruns a list about all the data about games in the region.
- region_game_names: Returns a list of names for games included in the region.
- region_runs: Returns a list of all the avalible data about runs in the region.
- region_run_ids: Retuns a list of the the unique id assosited with each of the runs.
- region_run_games: Returns a list of the games that the runs are for.
- region_run_levels: Returns a list of the levels that the runs are for.
- region_run_categories: Returns a list of the categories that the runs are for.
- region_run_status: Returns a list of the status's of the runs in the region.
- region_run_comments: Returns a list of the comments for the runs in the region.
- region_run_users: Returns a list of the the users who submitted the runs.
- region_run_submitted_date: Returns a list of the dates when the run was submitted.
- region_run_times: Returns a list of the time the runs took.
- region_run_platforms: Returns a list of the platforms used for the runs.