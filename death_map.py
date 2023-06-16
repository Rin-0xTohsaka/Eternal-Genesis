import pygame
import numpy as np

# Parameters
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 10
BACKGROUND_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize the state of the Game of Life
num_cells_wide = WIDTH // CELL_SIZE
num_cells_high = HEIGHT // CELL_SIZE
cells = np.zeros((num_cells_wide, num_cells_high, 2), dtype=int)
cells[..., 0] = np.random.choice([0, 1], num_cells_wide * num_cells_high).reshape((num_cells_wide, num_cells_high))

# Initialize the death map
death_map = np.zeros((num_cells_wide, num_cells_high), dtype=float)

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
                death_map[i, j] = 1  # Mark the cell as having died
            elif cells[i, j, 0] == 0 and total == 3:
                new_cells[i, j] = [1, 0]
            elif cells[i, j, 0] == 1:
                new_cells[i, j, 1] += 1

    cells = new_cells

    # Fade the death map
    death_map = np.maximum(death_map - 0.01, 0)

    # Draw the cells
    for i in range(num_cells_wide):
        for j in range(num_cells_high):
            if cells[i, j, 0] == 1:
                pygame.draw.circle(screen, (0, 255, 0), (i*CELL_SIZE, j*CELL_SIZE), CELL_SIZE // 2)
            elif death_map[i, j] > 0:
                pygame.draw.circle(screen, (int(death_map[i, j] * 255), 0, 0), (i*CELL_SIZE, j*CELL_SIZE), CELL_SIZE // 2)

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
