import speedrunapi as sr
import time

start = time.time()

def main_functions(user):
    print(user.lookup)
    print(user.id)
    print(user.name_style)
    print(user.role)
    print(user.signup)
    print(user.location)
    print(user.links)

def special_cases(user):
    print(user.runs)
    print(user.moderated_games)
    print(user.personal_bests)

user = sr.User('fishin_rod')
main_functions(user)
special_cases(user) 

end = time.time()
print(end-start)