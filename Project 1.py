import pygame
import random
pygame.init()

x = 500
y = 500
print(x,y)
window = pygame.display.set_mode((x,y))
pygame.display.set_caption("Project 1")

Blue=(100,100,100)
black =(0,0,0)
xpos = 0
ypos = 0
w = 30
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] > xpos and pygame.mouse.get_pos()[0] < xpos + w and
                pygame.mouse.get_pos()[1] > ypos and pygame.mouse.get_pos()[1] < ypos + w):
                xpos = round(random.randrange(20,x))
                ypos = round(random.randrange(20, y))
    window.fill(Blue)
    pygame.draw.rect(window,black,(xpos,ypos,w,w))
    pygame.display.update()