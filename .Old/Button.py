import pygame


class Button:
    def __init__(self, x, y, width, height, text, action,
                 font=pygame.font.Font(None, 36),
                 btn_clr=(0, 128, 255),
                 txt_clr = (255, 255, 255)):
        """
        :param x:
        :param y:
        :param width:
        :param height:
        :param text:
        :param action:
        :param font:
        :param btn_clr:
        :param txt_clr:
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.FONT = font
        self.BUTTON_COLOR = btn_clr
        self.TEXT_COLOR = txt_clr

    def draw(self, surface):
        pygame.draw.rect(surface, self.BUTTON_COLOR, self.rect)
        text_surface = self.FONT.render(self.text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

    def set_font(self, font):
        self.font = font

    def set_button_color(self, btn_clr):
        self.BUTTON_COLOR = btn_clr

    def set_text_color(self, txt_clr):
        self.TEXT_COLOR = txt_clr