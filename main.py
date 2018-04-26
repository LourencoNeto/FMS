from SimulatorModules import ManagerTeam
from menu import *
from selection_menu import *
from manager_menu import *
from game_menu import *

pygame.init()
name, quit = menu()
if not quit:
    team, quit = selection_menu()
if not quit:
    Manager_Team, quit = manager_menu(name, team)
opponents = OpponentsOrder(team)
number = 0
while not quit:
    Away_Team = opponents.get_opponent()
    away = opponents.get_opponent_name()
    quit = game_menu(team, away, Manager_Team, Away_Team)
    if not quit:
        Manager_Team, quit = manager_menu(name, team, Manager_Team)
    number += 1
    if number > 19:
        number = 0
pygame.quit()
