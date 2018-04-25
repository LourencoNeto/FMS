from SimulatorModules import *
import pandas as pd

database = pd.read_csv('Simulation/Database/FIFA18_database.csv')
#premier_league = database.loc[database.league == 'English Premier League']

team = 'Arsenal'
data_team = database.loc[database.club == team]

Manager_Team = ManagerTeam(data_team)
main_team = Manager_Team.get_list_team()
substitutes_team = Manager_Team.get_list_substitutes()
reserves_team = Manager_Team.get_list_reserves()

pygame.init()
pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.QUIT])
surface_height = 640
surface_width = 1080
main_surface = pygame.display.set_mode((surface_width, surface_height))
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()
MainTeamTable = SelectBoxTable(main_surface, main_team, 590, 140, 170, 20)
SubsTeamTable = SelectBoxTable(main_surface, substitutes_team, 320, 140, 170, 20)
ReservesTeamTable = SelectBoxTable(main_surface, reserves_team, 320, 330, 170, 20)
main_surface.fill((33, 94, 33))
main_surface.blit(font.render("Substitutos:", True, pygame.Color("black")), (320, 310))
main_surface.blit(font.render("Time Titular:", True, pygame.Color("black")), (590, 120))
main_surface.blit(font.render("Reservas:", True, pygame.Color("black")), (320, 120))
main_surface.blit(font.render("Formação:", True, pygame.Color("black")), (50, 310))
table_selected1 = ''
table_selected2 = ''
player1 = ''
player2 = ''
alternation = 0
done = False
while not done:
    for ev in pygame.event.get():
        if not done:
            MainTeamTable.handle_event(ev)
            SubsTeamTable.handle_event(ev)
            ReservesTeamTable.handle_event(ev)
        if ev.type == pygame.QUIT:
            done = True
            break
        if MainTeamTable.activity():
            if alternation == 0:
                player1 = MainTeamTable.selected_box().get_text()
                table_selected1 = 'team'
                alternation = 1
            else:
                player2 = MainTeamTable.selected_box().get_text()
                table_selected2 = 'team'
                alternation == 0
        if SubsTeamTable.activity():
            if alternation == 0:
                player1 = SubsTeamTable.selected_box().get_text()
                table_selected1 = 'substitutes'
                alternation = 1
            else:
                player2 = SubsTeamTable.selected_box().get_text()
                table_selected2 = 'substitutes'
                alternation == 0

        if ReservesTeamTable.activity():
            if alternation == 0:
                player1 = ReservesTeamTable.selected_box().get_text()
                table_selected1 = 'reserves'
                alternation = 1
            else:
                player2 = ReservesTeamTable.selected_box().get_text()
                table_selected2 = 'reserves'
                alternation = 0

        if not MainTeamTable.activity() and not SubsTeamTable.activity() and not ReservesTeamTable.activity():
            table_selected1 = ''
            table_selected2 = ''
            player1 = ''
            player2 = ''
            alternation = 0

        if table_selected1 != '' and table_selected2 != '':
            Manager_Team.switches(table_selected1, player1, table_selected2, player2)
            main_team = Manager_Team.get_list_team()
            substitutes_team = Manager_Team.get_list_substitutes()
            reserves_team = Manager_Team.get_list_reserves()
            MainTeamTable.update_table(main_team)
            SubsTeamTable.update_table(substitutes_team)
            ReservesTeamTable.update_table(reserves_team)
            table_selected1 = ''
            table_selected2 = ''
            player1 = ''
            player2 = ''
            alternation = 0
    MainTeamTable.draw()
    SubsTeamTable.draw()
    ReservesTeamTable.draw()
    pygame.display.flip()

pygame.quit()
