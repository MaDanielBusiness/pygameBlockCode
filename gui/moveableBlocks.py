import pygame

class MovableRectangle:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.clicked = False
        self.offset_x = 0
        self.offset_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.clicked = True
                    self.offset_x = mouse_x - self.rect.x
                    self.offset_y = mouse_y - self.rect.y

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.clicked = False

    def update(self):
        if self.clicked:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.x = mouse_x - self.offset_x
            self.rect.y = mouse_y - self.offset_y

class Button:
    def __init__(self, x, y, width, height, color, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.callback()

# Pygame initialization
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangles")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create a list of movable rectangles
rectangles = []

# Function to add a new movable rectangle
def add_rectangle():
    new_rectangle = MovableRectangle(100, 100, 100, 50, RED)
    rectangles.append(new_rectangle)

# Create a button to add new rectangles
add_button = Button(50, 50, 200, 50, BLUE, "Add Rectangle", add_rectangle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for rectangle in rectangles:
            rectangle.handle_event(event)

        add_button.handle_event(event)

    window.fill(WHITE)

    for rectangle in rectangles:
        rectangle.update()
        rectangle.draw(window)

    add_button.draw(window)

    pygame.display.flip()

pygame.quit()