import pygame

class StackableBlock:
    """
    The StackableBlock is a block that has a before, inside, and an after StackableBlock
    It should also have an associated script that it should be able to run
    """
    def __init__(self, x=200, y=100, width=200, height=100, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

        self.prev = None
        self.inner = None
        self.after = None
        self.command = None

    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def set_prev(self, prev_block):
        self.prev = prev_block

    def set_inner(self, inner_block):
        self.inner = inner_block

    def set_after(self, after_block):
        self.after = after_block

    def set_command(self, command):
        self.command = command



    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)