import pygame
import random

GRID_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 16
WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE

def draw_grid(screen):
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (WINDOW_WIDTH, y))

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        # Initial mole position
        mole_x, mole_y = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    grid_x, grid_y = mouse_x // GRID_SIZE, mouse_y // GRID_SIZE
                    if grid_x == mole_x and grid_y == mole_y:
                        mole_x = random.randrange(0, GRID_WIDTH)
                        mole_y = random.randrange(0, GRID_HEIGHT)

            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * GRID_SIZE, mole_y * GRID_SIZE)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()