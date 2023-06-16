import pygame
import numpy as np

# Parameters
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 10
BACKGROUND_COLOR = (0, 0, 0)
CELL_COLOR = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize the state of the Game of Life
num_cells_wide = WIDTH // CELL_SIZE
num_cells_high = HEIGHT // CELL_SIZE
cells = np.random.choice([0, 1], num_cells_wide * num_cells_high).reshape((num_cells_wide, num_cells_high))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Compute the next state of the Game of Life
    new_cells = cells.copy()
    for i in range(num_cells_wide):
        for j in range(num_cells_high):
            total = (cells[i, (j-1)%num_cells_high] + cells[i, (j+1)%num_cells_high] +
                     cells[(i-1)%num_cells_wide, j] + cells[(i+1)%num_cells_wide, j] +
                     cells[(i-1)%num_cells_wide, (j-1)%num_cells_high] + cells[(i-1)%num_cells_wide, (j+1)%num_cells_high] +
                     cells[(i+1)%num_cells_wide, (j-1)%num_cells_high] + cells[(i+1)%num_cells_wide, (j+1)%num_cells_high])
            if cells[i, j] == 1 and (total < 2 or total > 3):
                new_cells[i, j] = 0
            elif cells[i, j] == 0 and total == 3:
                new_cells[i, j] = 1

    cells = new_cells

    # Draw the cells
    for i in range(num_cells_wide):
        for j in range(num_cells_high):
            if cells[i, j] == 1:
                pygame.draw.rect(screen, CELL_COLOR, pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Flip the display
    pygame.display.flip()
    pygame.time.wait(100)  # Delay in milliseconds


# Quit Pygame
pygame.quit()
