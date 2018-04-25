from SimulatorModules import *
import pandas as pd


def selection_menu():
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.QUIT])
    surface_height = 540
    surface_width = 240
    main_surface = pygame.display.set_mode((surface_width, surface_height))
    font = pygame.font.SysFont(None, 20)

    database = pd.read_csv('Simulation/Database/FIFA18_database.csv')
    premier_league = database.loc[database.league == 'English Premier League']
    english_teams = premier_league.club.unique().tolist()
    Table = SelectBoxTable(main_surface, english_teams, 40, 40, 170, 20)
    Next_Button = Button(130, 490, 100, 40, 40, 13, "Next")
    main_surface.fill((33, 94, 33))
    main_surface.blit(font.render("Selecione seu time:", True, pygame.Color("black")), (10, 10))
    Next_Button.draw(main_surface)
    done = False
    quit = False
    team = ''
    while not done:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done = True
                quit = True
                break
            if Next_Button.handle_event(ev):
                active = Table.activity()
                if active:
                    selected = Table.selected_box()
                    team = selected.get_text()
                    done = True
                    Next_Button.draw(main_surface)
                    break
            if not done:
                Table.handle_event(ev)
        Table.draw()
        pygame.display.flip()
    return team, quit
