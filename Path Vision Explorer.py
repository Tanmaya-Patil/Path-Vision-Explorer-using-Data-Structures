import pygame
import sys
from collections import deque
import math
import random

# Constants for colors and window size
WHITE = 255, 255, 255
BLACK = 0, 0, 0
LIGHT_BLUE = 189, 201, 225
DARK_BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

size = (width, height) = 1280, 720
pygame.init()

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False

    def show(self, win, col):
        if self.wall:
            col = BLACK
        pygame.draw.rect(win, col, (self.x * w, self.y * h, w - 1, h - 1))

    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])

def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state

cols, rows = 64, 48
w = width // cols
h = height // rows
grid = []
for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)

start = grid[cols // 2][rows // 2]
end = grid[cols - 1][rows - cols // 2]
start.wall = False
end.wall = False

def generate_start_end():
    global start, end
    start = grid[random.randint(0, cols - 1)][random.randint(0, rows - 1)]
    end = grid[random.randint(0, cols - 1)][random.randint(0, rows - 1)]

    while start == end:  # Ensure start and end points are different
        end = grid[random.randint(0, cols - 1)][random.randint(0, rows - 1)]

    start.wall = False
    end.wall = False

def dijkstra():
    global grid
    queue = deque()
    visited = []
    path = []

    queue.append(start)
    start.visited = True

    while queue:
        current = queue.popleft()
        if current == end:
            temp = current
            while temp.prev:
                path.append(temp.prev)
                temp = temp.prev
            print("Dijkstra's Solution found")
            for spot in path:
                spot.visited = False
            return path[::-1]  # Return path in reverse order for visualization

        for i in current.neighbors:
            if not i.visited and not i.wall:
                i.visited = True
                i.prev = current
                queue.append(i)
                visited.append(i)

        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, WHITE)
                if spot.visited:
                    spot.show(win, RED)
                if spot in queue:
                    spot.show(win, GREEN)
                if spot == start:
                    spot.show(win, DARK_BLUE)
                if spot == end:
                    spot.show(win, DARK_BLUE)
        pygame.display.flip()

def bfs():
    global grid
    queue = deque()
    visited = []
    path = []

    queue.append(start)
    start.visited = True

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = queue.popleft()
        if current == end:
            temp = current
            while temp.prev:
                path.append(temp.prev)
                temp = temp.prev
            print("BFS Solution found")
            for spot in path:
                spot.visited = False
            return path[::-1]  # Return path in reverse order for visualization

        for i in current.neighbors:
            if not i.visited and not i.wall:
                i.visited = True
                i.prev = current
                queue.append(i)
                visited.append(i)

        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, WHITE)
                if spot.visited:
                    spot.show(win, RED)
                if spot in queue:
                    spot.show(win, GREEN)
                if spot == start:
                    spot.show(win, DARK_BLUE)
                if spot == end:
                    spot.show(win, DARK_BLUE)
        pygame.display.flip()


def dfs():
    global grid
    stack = deque()
    visited = []
    path = []

    stack.append(start)
    start.visited = True

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = stack.pop()
        if current == end:
            temp = current
            while temp.prev:
                path.append(temp.prev)
                temp = temp.prev
            print("DFS Solution found")
            for spot in path:
                spot.visited = False
            return path[::-1]  # Return path in reverse order for visualization

        for i in current.neighbors:
            if not i.visited and not i.wall:
                i.visited = True
                i.prev = current
                stack.append(i)
                visited.append(i)

        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, WHITE)
                if spot.visited:
                    spot.show(win, RED)
                if spot in stack:
                    spot.show(win, GREEN)
                if spot == start:
                    spot.show(win, DARK_BLUE)
                if spot == end:
                    spot.show(win, DARK_BLUE)
        pygame.display.flip()

# Initialize Pygame
pygame.init()
win = pygame.display.set_mode(size)
pygame.display.set_caption('Path Vision Explorer using Data Structures')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
bfs_path = []
dfs_path = []
dijkstra_path = []

reset_grid = False

text_dijkstra = font.render("Dijkstra - Enter", True, BLACK)
text_bfs = font.render("BFS - B", True, BLACK)
text_dfs = font.render("DFS - D", True, BLACK)
text_reset = font.render("RESET - R", True, BLACK)

text_width = text_dijkstra.get_width() + text_bfs.get_width() + text_dfs.get_width() + text_reset.get_width()
spacing = 20  # Adjust the spacing between the texts

text_dijkstra_pos = text_dijkstra.get_rect(center=(width // 2 - text_width // 2 + text_dijkstra.get_width() // 2, 30))
text_bfs_pos = text_bfs.get_rect(center=(text_dijkstra_pos.right + text_bfs.get_width() // 2 + spacing, 30))
text_dfs_pos = text_dfs.get_rect(center=(text_bfs_pos.right + text_dfs.get_width() // 2 + spacing, 30))
text_reset_pos = text_reset.get_rect(center=(text_dfs_pos.right + text_reset.get_width() // 2 + spacing, 30))

drawing_wall = False  # Flag to track if the mouse button is held down

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:  # Press 'b' for BFS
                bfs_path = bfs()
                if bfs_path:
                    for spot in bfs_path:
                        spot.show(win, LIGHT_BLUE)
            elif event.key == pygame.K_d:  # Press 'd' for DFS
                dfs_path = dfs()
                if dfs_path:
                    for spot in dfs_path:
                        spot.show(win, LIGHT_BLUE)
            elif event.key == pygame.K_RETURN:
                dijkstra_path = dijkstra()
                if dijkstra_path:
                    for spot in dfs_path:
                        spot.show(win, LIGHT_BLUE)
            elif event.key == pygame.K_r:  # Press 'r' to reset
                reset_grid = True
                for i in range(cols):
                    for j in range(rows):
                        grid[i][j].visited = False
                        grid[i][j].prev = None
                        bfs_path = []
                        dfs_path = []
                        dijkstra_path = []
                        grid[i][j].wall = False
                generate_start_end() 
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (1, 3):
                clickWall(pygame.mouse.get_pos(), event.button == 1)
                drawing_wall = True  # Set flag to indicate the mouse button is being held

        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0] or event.buttons[2]:
                clickWall(pygame.mouse.get_pos(), event.buttons[0])

        if event.type == pygame.MOUSEBUTTONUP:
            drawing_wall = False  # Reset flag when the mouse button is released

    win.fill((0, 20, 20))
    for i in range(cols):
        for j in range(rows):
            spot = grid[i][j]
            if spot == start or spot == end:
                spot.show(win, DARK_BLUE)
            else:
                if spot in bfs_path or spot in dfs_path or spot in dijkstra_path:
                    spot.show(win, LIGHT_BLUE)
                else:
                    spot.show(win, WHITE)

    win.blit(text_dijkstra, text_dijkstra_pos)
    win.blit(text_bfs, text_bfs_pos)
    win.blit(text_dfs, text_dfs_pos)
    win.blit(text_reset, text_reset_pos)

    pygame.display.flip()
    clock.tick(60)
