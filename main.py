import pygame
import sys
import os
from Button import Button  # Import the Button class from the button module


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

# Load window position and size data if the file exists
if os.path.exists(window_data_file):
    with open(window_data_file, "r") as file:
        data = file.readline().strip().split(",")
        if len(data) == 4:
            default_x, default_y, default_width, default_height = map(int, data)

# Create the main window
screen = pygame.display.set_mode((default_width, default_height), pygame.RESIZABLE)
pygame.display.set_caption("Pygame GUI")


# Create buttons with lambda functions
button1 = Button(50, 100, 100, 50, "Button 1",
                 lambda: add_command(command_list ,"Button 1 Clicked"))
button2 = Button(250, 100, 100, 50, "Button 2",
                 lambda: add_command(command_list ,"Button 2 Clicked"))

# Set some button details
for button in [button1, button2]:
    button.set_font(FONT)
    button.set_button_color(BUTTON_COLOR)
    button.set_text_color(TEXT_COLOR)

# Create a list of commands to be executed
command_list = []

# Function to add commands to the list
def add_command(command_list, command):
    command_list.append(command)

def run_commands(command_list:list):
    """
    Take a list of functions and run them
    Should be called from the GUI
    """
    command: object
    for command in command_list:
        var = lambda: command

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
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Handle window resize
            default_width, default_height = event.size
            screen = pygame.display.set_mode((default_width, default_height), pygame.RESIZABLE)
        for button in [button1, button2]:
            button.handle_event(event)

    screen.fill(BACKGROUND_COLOR)

    # Draw buttons
    button1.draw(screen)
    button2.draw(screen)

    # Display command blocks
    display_commands(screen)

    pygame.display.flip()

# Save window position and size data to a file
with open(window_data_file, "w") as file:
    file.write(f"{default_x},{default_y},{default_width},{default_height}")

# Quit Pygame
pygame.quit()
sys.exit()
