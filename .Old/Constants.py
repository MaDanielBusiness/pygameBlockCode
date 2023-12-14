import sys

import pygame

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