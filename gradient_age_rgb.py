import pygame
import numpy as np

# Parameters
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 10
BACKGROUND_COLOR = (0, 0, 0)
MAX_AGE = 255  # Max age used for color calculation.

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize the state of the Game of Life
num_cells_wide = WIDTH // CELL_SIZE
num_cells_high = HEIGHT // CELL_SIZE
cells = np.zeros((num_cells_wide, num_cells_high, 2), dtype=int)
cells[..., 0] = np.random.choice([0, 1], num_cells_wide * num_cells_high).reshape((num_cells_wide, num_cells_high))

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
            total = (cells[i, (j-1)%num_cells_high, 0] + cells[i, (j+1)%num_cells_high, 0] +
                     cells[(i-1)%num_cells_wide, j, 0] + cells[(i+1)%num_cells_wide, j, 0] +
                     cells[(i-1)%num_cells_wide, (j-1)%num_cells_high, 0] + cells[(i-1)%num_cells_wide, (j+1)%num_cells_high, 0] +
                     cells[(i+1)%num_cells_wide, (j-1)%num_cells_high, 0] + cells[(i+1)%num_cells_wide, (j+1)%num_cells_high, 0])
            if cells[i, j, 0] == 1 and (total < 2 or total > 3):
                new_cells[i, j] = [0, 0]
            elif cells[i, j, 0] == 0 and total == 3:
                new_cells[i, j] = [1, 0]
            elif cells[i, j, 0] == 1:
                new_cells[i, j, 1] += 1

    cells = new_cells

    # Draw the cells
    for i in range(num_cells_wide):
        for j in range(num_cells_high):
            if cells[i, j, 0] == 1:
                age_color = min(255, cells[i, j, 1] * 5)  # Scale the color change rate.
                total_neighbors = (cells[i, (j-1)%num_cells_high, 0] + cells[i, (j+1)%num_cells_high, 0] +
                                   cells[(i-1)%num_cells_wide, j, 0] + cells[(i+1)%num_cells_wide, j, 0] +
                                   cells[(i-1)%num_cells_wide, (j-1)%num_cells_high, 0] + cells[(i-1)%num_cells_wide, (j+1)%num_cells_high, 0] +
                                   cells[(i+1)%num_cells_wide, (j-1)%num_cells_high, 0] + cells[(i+1)%num_cells_wide, (j+1)%num_cells_high, 0])
                neighbor_color = int(total_neighbors * 255 / 8)  # Scale the color based on neighbor count.
                pygame.draw.rect(screen, (neighbor_color, age_color, 255 - age_color), pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
