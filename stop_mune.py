from SimulatorModules import *
import pandas as pd

def stop_menu(Manager_Team, team):

    main_team = Manager_Team.get_list_team()
    substitutes_team = Manager_Team.get_list_substitutes()
    reserves_team = Manager_Team.get_list_reserves()
    list_formation = Manager_Team.get_list_formation()

    pygame.init()
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.QUIT])
    surface_height = 450
    surface_width = 570
    main_surface = pygame.display.set_mode((surface_width, surface_height))
    font1 = pygame.font.SysFont(None, 20)
    clock = pygame.time.Clock()
    FormationTable = SelectBoxTable(main_surface, Manager_Team.get_possible_formation(), 50, 260, 100, 20)
    IndexTable = SelectBoxTable(main_surface, list_formation, 320, 70, 30, 20)
    MainTeamTable = SelectBoxTable(main_surface, main_team, 350, 70, 170, 20)
    SubsTeamTable = SelectBoxTable(main_surface, substitutes_team, 50, 70, 170, 20)
    Restart_Button = Button(350, 360, 180, 40, 34, 13, "Recomeçar Partida")
    main_surface.fill((33, 94, 33))
    main_surface.blit(font1.render("Time Titular:", True, pygame.Color("black")), (320, 50))
    main_surface.blit(font1.render("Banco de Reservas:", True, pygame.Color("black")), (50, 50))
    main_surface.blit(font1.render("Formação:", True, pygame.Color("black")), (50, 240))
    table_selected1 = ''
    table_selected2 = ''
    player1 = ''
    player2 = ''
    alternation = 0
    altered_formation = False
    quit = False
    done = False
    while not done:
        for ev in pygame.event.get():
            if not done:
                MainTeamTable.handle_event(ev)
                SubsTeamTable.handle_event(ev)
                FormationTable.handle_event(ev)
            if ev.type == pygame.QUIT:
                done = True
                quit = True
                break
            if FormationTable.activity():
                formation = FormationTable.selected_box().get_text()
                if formation == "     4 - 4 - 2":
                    if Manager_Team.get_formation() != 442:
                        altered_formation = True
                    Manager_Team.set_formation(442)
                if formation == "     4 - 3 - 3":
                    if Manager_Team.get_formation() != 433:
                        altered_formation = True
                    Manager_Team.set_formation(433)
                if formation == "     5 - 3 - 2":
                    if Manager_Team.get_formation() != 532:
                        altered_formation = True
                    Manager_Team.set_formation(532)
                if formation == "     3 - 5 - 2":
                    if Manager_Team.get_formation() != 352:
                        altered_formation = True
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
            if not MainTeamTable.activity() and not SubsTeamTable.activity():
                table_selected1 = ''
                table_selected2 = ''
                player1 = ''
                player2 = ''
                alternation = 0
            if table_selected1 != '' and table_selected2 != '':
                Manager_Team.switches(table_selected1, player1, table_selected2, player2)
                main_team = Manager_Team.get_list_team()
                substitutes_team = Manager_Team.get_list_substitutes()
                MainTeamTable.update_table(main_team)
                SubsTeamTable.update_table(substitutes_team)
                table_selected1 = ''
                table_selected2 = ''
                player1 = ''
                player2 = ''
                alternation = 0
            done = Restart_Button.handle_event(ev)
        Restart_Button.draw(main_surface)
        IndexTable.draw()
        FormationTable.draw()
        MainTeamTable.draw()
        SubsTeamTable.draw()
        pygame.display.flip()
    return altered_formation, Manager_Team.get_team(), Manager_Team.get_formation(), quit
