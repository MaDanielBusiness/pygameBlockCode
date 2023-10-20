import pygame
import sys
import os

import Constants
from Button import Button  # Import the Button class from the button module
from Constants import *


# Initialize Pygame
#pygame.init()

x, y, win_width, win_height = Constants.default_x, Constants.default_y, Constants.default_width, Constants.default_height

# Load window position and size data if the file exists
if os.path.exists(window_data_file):
    with open(window_data_file, "r") as file:
        data = file.readline().strip().split(",")
        if len(data) == 4:
            x, y, win_width, win_height = map(int, data)

# Create the main window
screen = pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
pygame.display.set_caption("Pygame GUI")


# Create buttons with lambda functions
button_list = [
    Button(50, 100, 100, 50, "Button 1",
           lambda: add_command(command_list, "Button 1 Clicked")),
    Button(250, 100, 100, 50, "Button 2",
           lambda: add_command(command_list ,"Button 2 Clicked"))
]

# Set some button details
for button in button_list:
    button.set_font(Constants.FONT)
    button.set_button_color(Constants.BUTTON_COLOR)
    button.set_text_color(Constants.TEXT_COLOR)

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
        pygame.draw.rect(surface, Constants.BUTTON_COLOR, (50, y_offset, 300, 50))
        text_surface = Constants.FONT.render(command, True, Constants.TEXT_COLOR)
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
            win_width, win_height = event.size
            screen = pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
        for button in button_list:
            button.handle_event(event)

    screen.fill(Constants.BACKGROUND_COLOR)

    # Draw buttons
    for button in button_list:
        button.draw(screen)

    # Display command blocks
    display_commands(screen)

    pygame.display.flip()

# Save window position and size data to a file
with open(window_data_file, "w") as file:
    file.write(f"{x},{y},{win_width},{win_height}")

# Quit Pygame
pygame.quit()
sys.exit()
