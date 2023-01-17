Users
===
Speedrun.com allows you to query for user data, the user class allows you to get this data using this library.
<br>
To initialize a user object you use the following code replacing fishin_rod with the username you are trying to look for, and replacing user with the variable name you want associated with the user inputed. 
<br>
The class takes one parameter, a username stored as a string in a variable or a string, 0 or 2+ parameters entered will give a type error.
```python
user = speedrunapi.User("fishin_rod")
```
Great! You have set up a user object, now its time to do operations on that user object.
<br>
To do opperations on a user, just add one of the supported operations to the user object.
<br>
If you do the opperation id to the user it will return the id of the user put into the program.
```python
>>> print(user.id)
jonryvl8
```
Or you can do it directly to the user object.
```python
>>> print(speedrunapi.User("fishin_rod").id)
jonryvl8
```
Currently supported operations:
===
- lookup: Returns the profile data of the user in a dictionary format
- id: Returns the ID of the user as a string
- name_style: Returns the name style a user has on speedrun.com as a dictonary
- role: Returns the role of the user as a string, possible values: 
- signup: Returns the join date of the user as a string in the format Y/M/D H/M/S
- location: Returns the location of the user as a dictionary containing information about the country and region
- links: Returns the links the user has listed on their profiles as a list (can be None)
- moderated_games: Returns the games the user moderates as a dictionary
- personal_bests: Returns the personal bests of the user in a dictionary format
