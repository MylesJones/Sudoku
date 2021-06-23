import pygame

pygame.init()

BOARD_WIDTH = 800

screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_WIDTH))

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))


    # Flip the display
    pygame.display.flip()

class Board:
    def __init__(self):
        self.grid = [[]]
