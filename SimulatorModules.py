import pygame


class InputBox:

    def __init__(self, x, y, width, text=''):
        self.height = 20
        self.rect = pygame.Rect(x, y, width, self.height)
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_text = pygame.Color("black")
        self.color_rect = self.color_inactive
        self.color_background = pygame.Color("white")
        self.text = text
        self.font = pygame.font.Font(None, 20)
        self.text_surface = self.font.render(self.text, True, self.color_text)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                print("1")      ###################################################################################################################
            else:
                self.active = False
            self.color_rect = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode ##eliminar os casos em que nao sao simbolos, letras ou numeros e colocar um limite no tamanho da palavra
            self.text_surface = self.font.render(self.text, True, self.color_text)

    def draw(self, main_surface):
        main_surface.fill(self.color_background, self.rect)
        main_surface.blit(self.text_surface, (self.rect.x+5,self.rect.y+2))
        pygame.draw.rect(main_surface, self.color_rect, self.rect, 1)

    def get_text(self):
        return self.text


class Button:

    def __init__(self, x, y, width, height, dx, dy, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_text = pygame.Color("black")
        self.color_rect = self.color_inactive
        self.color_background = pygame.Color("white")
        self.text = text
        self.font = pygame.font.Font(None, 20)
        self.text_surface = self.font.render(self.text, True, self.color_text)
        self.dx = dx
        self.dy = dy

    def draw(self, main_surface):
        main_surface.fill(self.color_background, self.rect)
        main_surface.blit(self.text_surface, (self.rect.x + self.dx, self.rect.y + self.dy))
        pygame.draw.rect(main_surface, self.color_rect, self.rect, 1)

    def handle_event(self, event, main_surface):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("2")  #############################################################################################
                self.color_rect = self.color_active
                self.draw(main_surface)
                return True
            else: return False


class SelectBox:
    def __init__(self, x, y, width, text=''):
        self.height = 20
        self.rect = pygame.Rect(x, y, width, self.height)
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_text = pygame.Color("black")
        self.color_rect = self.color_inactive
        self.color_background = pygame.Color("white")
        self.text = text
        self.font = pygame.font.Font(None, 20)
        self.text_surface = self.font.render(self.text, True, self.color_text)
        self.active = False


    def draw(self, main_surface):
        main_surface.fill(self.color_background, self.rect)
        main_surface.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 2))
        pygame.draw.rect(main_surface, self.color_rect, self.rect, 1)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                print("1")      ###################################################################################################################
            else:
                self.active = False
            self.color_rect = self.color_active if self.active else self.color_inactive

    def get_text(self):
        return self.text