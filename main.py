import generate
import pygame
import numpy as np

SIZE = 600

def run():
    maze = generate.create_maze()
    pygame.init()
    display = pygame.display.set_mode(size=(SIZE, SIZE))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        skip_y = int(SIZE / len(maze[0]))
        skip_x = int(SIZE / len(maze))

        for x in range(0, SIZE, skip_x):
            for y in range(0, SIZE, skip_y):
                rect = pygame.Rect(x,y, SIZE / len(maze), SIZE / len(maze[0]))
                pygame.draw.rect(display, (255,255,255), rect, 1)
                # print(int(x/skip_x), int(y/skip_y))
                if not maze[int(y / skip_y)][int(x / skip_x)].walls['top']:
                    print(x/skip_x, y/skip_y)
                    print(x, y)
                    pygame.draw.line(display, (0,0,0), (x,y), (x + skip_x,y), 3)
                if not maze[int(y / skip_y)][int(x / skip_x)].walls['left']:
                    pygame.draw.line(display, (0,0,0), (x,y), (x,y + skip_y), 3)
        
        pygame.display.update()


        

if __name__ == '__main__':
    run()