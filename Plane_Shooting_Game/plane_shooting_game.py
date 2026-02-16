# 2d length and height plane game where you rotate your plane and shoot down others

import pygame
import os

pygame.init()
screen_width, screen_height = 1200, 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Star Wars Army Game")
font = pygame.font.SysFont("arial", 15)
clock = pygame.time.Clock()
fps = 60
#game variables and images