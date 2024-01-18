import pygame

class InputField:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.input_text = ''
        self.active = False
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.rect = pygame.Rect(850, 600, 200, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        player_count = int(self.input_text)
                        if player_count > 0:
                            return player_count
                        else:
                            self.input_text = ''
                    except ValueError:
                        self.input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode if event.unicode.isnumeric() else ''

    def update(self):
        width = max(200, self.font.size(self.input_text)[0] + 10)
        self.rect.w = width

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
        text = self.font.render(self.input_text, True, self.color)
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)