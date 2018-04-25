from SimulatorModules import *

def menu():
    pygame.init()
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.QUIT, pygame.KEYDOWN])
    name = ''
    surface_height = 360
    surface_width = 480
    main_surface = pygame.display.set_mode((surface_width, surface_height))
    font = pygame.font.Font(None, 20)
    small_rect = (260, 60, 210, 200)
    some_color = (50, 205, 50)
    clock = pygame.time.Clock()
    Box = InputBox(320, 110, 140)
    Start_Button = Button(315, 200, 100, 40, 34, 13, "Start")
    main_surface.fill((33, 94, 33))
    main_surface.fill(some_color, small_rect)
    main_surface.blit(font.render("Nome:", True, pygame.Color("black")), (270, 112))
    Start_Button.draw(main_surface)
    done = False
    quit = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done = True
                quit = True
                break
            Box.handle_event(ev)
            done = Start_Button.handle_event(ev)
        if done:
            name = Box.get_text()
            Start_Button.draw(main_surface)
        Box.draw(main_surface)
        pygame.display.flip()
        clock.tick(30)
    return name, quit
