from SimulatorModules import *
import pandas as pd


def manager_menu(name, team, Manager = None):
    database = pd.read_csv('Simulation/Database/FIFA18_database.csv')

    next_opponent = 'Liverpool'
    if Manager is None:
        data_team = database.loc[database.club == team]
        Manager_Team = ManagerTeam(data_team)

    main_team = Manager_Team.get_list_team()
    substitutes_team = Manager_Team.get_list_substitutes()
    reserves_team = Manager_Team.get_list_reserves()
    list_formation = Manager_Team.get_list_formation()

    pygame.init()
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.QUIT])
    surface_height = 560
    surface_width = 770
    main_surface = pygame.display.set_mode((surface_width, surface_height))
    font1 = pygame.font.SysFont(None, 20)
    font2 = pygame.font.SysFont(None, 40)
    clock = pygame.time.Clock()
    FormationTable = SelectBoxTable(main_surface, Manager_Team.get_possible_formation(), 50, 330, 100, 20)
    IndexTable = SelectBoxTable(main_surface, list_formation, 520, 140, 30, 20)
    MainTeamTable = SelectBoxTable(main_surface, main_team, 550, 140, 170, 20)
    SubsTeamTable = SelectBoxTable(main_surface, substitutes_team, 250, 140, 170, 20)
    ReservesTeamTable = SelectBoxTable(main_surface, reserves_team, 250, 330, 170, 20)
    Start_Button = Button(550, 430, 170, 40, 34, 13, "Começar Partida")
    main_surface.fill((33, 94, 33))
    main_surface.blit(font1.render("Time Substituto:", True, pygame.Color("black")), (250, 310))
    main_surface.blit(font1.render("Time Titular:", True, pygame.Color("black")), (520, 120))
    main_surface.blit(font1.render("Banco de Reservas:", True, pygame.Color("black")), (250, 120))
    main_surface.blit(font1.render("Formação:", True, pygame.Color("black")), (50, 310))
    main_surface.blit(font2.render(team, True, pygame.Color("black")), (25, 20))
    main_surface.blit(font1.render("Treinador: " + name, True, pygame.Color("black")), (25, 60))
    main_surface.blit(font1.render("Proximo oponente:", True, pygame.Color("black")), (50, 120))
    table_selected1 = ''
    table_selected2 = ''
    player1 = ''
    player2 = ''
    alternation = 0
    quit = False
    done = False
    while not done:
        for ev in pygame.event.get():
            if not done:
                MainTeamTable.handle_event(ev)
                SubsTeamTable.handle_event(ev)
                ReservesTeamTable.handle_event(ev)
                FormationTable.handle_event(ev)
            if ev.type == pygame.QUIT:
                done = True
                quit = True
                break
            if FormationTable.activity():
                formation = FormationTable.selected_box().get_text()
                if formation == "     4 - 4 - 2":
                    Manager_Team.set_formation(442)
                if formation == "     4 - 3 - 3":
                    Manager_Team.set_formation(433)
                if formation == "     5 - 3 - 2":
                    Manager_Team.set_formation(532)
                if formation == "     3 - 5 - 2":
                    Manager_Team.set_formation(352)
                IndexTable.update_table(Manager_Team.get_list_formation())
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
            done = Start_Button.handle_event(ev)
        Start_Button.draw(main_surface)
        IndexTable.draw()
        FormationTable.draw()
        MainTeamTable.draw()
        SubsTeamTable.draw()
        ReservesTeamTable.draw()
        pygame.display.flip()
    pygame.quit()
    return Manager_Team, quit