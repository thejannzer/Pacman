#main
from maze import Maze
#from pacman import Pacman
#from ghost import Ghost
#from pellet import Pellet
import pygame

pygame.init()

maze = Maze()
#pacman = Pacman()
#ghost = Ghost()
running = True

screen = pygame.display.set_mode((maze.WIDTH, maze.HEIGHT))
pygame.display.set_caption("Pac-Man")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    maze.draw_map(screen, maze.LEVEL)
    pygame.display.flip()
pygame.quit()


