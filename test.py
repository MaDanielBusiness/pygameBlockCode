import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
BACKGROUND_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 128, 255)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# File to store window position and size data
window_data_file = "window_data.txt"

# Default window position and size
default_width, default_height = 400, 300
default_x, default_y = 200, 100

# Function to save window position and size data to a file
def save_window_data():
    with open(window_data_file, "w") as file:
        file.write(f"{default_x},{default_y},{default_width},{default_height}")

# Load window position and size data if the file exists
if os.path.exists(window_data_file):
    with open(window_data_file, "r") as file:
        data = file.readline().strip().split(",")
        if len(data) == 4:
            default_x, default_y, default_width, default_height = map(int, data)

# Create the main window
screen = pygame.display.set_mode((default_width, default_height), pygame.RESIZABLE)
pygame.display.set_caption("Pygame GUI")


# Define a Button class
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, BUTTON_COLOR, self.rect)
        text_surface = FONT.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

# Create buttons with lambda functions
button1 = Button(50, 100, 100, 50, "Button 1", lambda: add_command("Button 1 Clicked"))
button2 = Button(250, 100, 100, 50, "Button 2", lambda: add_command("Button 2 Clicked"))

# Create a list of commands to be executed
command_list = []

# Function to add commands to the list
def add_command(command):
    command_list.append(command)

# Function to display the command blocks
def display_commands(surface):
    y_offset = 200  # Vertical position for displaying commands
    for command in command_list:
        pygame.draw.rect(surface, BUTTON_COLOR, (50, y_offset, 300, 50))
        text_surface = FONT.render(command, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(midleft=(60, y_offset + 25))
        surface.blit(text_surface, text_rect)
        y_offset += 60  # Increase the vertical position for the next block

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save window position and size data to a file before exiting
            save_window_data()
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Handle window resize and update window position
            default_width, default_height = event.size
            screen = pygame.display.set_mode((default_width, default_height), pygame.RESIZABLE)
            default_x, default_y = event.dict['x'], event.dict['y']
            save_window_data()  # Save the updated position
        for button in [button1, button2]:
            button.handle_event(event)

    screen.fill(BACKGROUND_COLOR)

    # Draw buttons
    button1.draw(screen)
    button2.draw(screen)

    # Display command blocks
    display_commands(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()