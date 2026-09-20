import heapq
import os
import time

# The maze grid

maze_grid = [
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,1],
    [0,0,0,0,0]
]

def animate_search(grid,start,end,visited_cells,active_queue,came_from,current_pos):

    os.system("cls" if os.name == 'nt' else "clear")

    rows,cols = len(grid), len(grid[0])

    queue_coords = {pos for _, pos in active_queue}

    print("DIJKSTRAS ALGORITHM ANIMATION... : \n\n")

    for r in range(rows):

        row_str = ""

        for c in range(cols):

            pos = (r,c)

            if pos == start:
                row_str += "🟢"
            elif pos == end:
                row_str += "🔴"
            elif pos == current_pos:
                row_str += "🎯"
            elif pos in queue_coords:
                row_str += "🟡"
            elif pos in visited_cells:
                row_str = "🔍"
            elif grid[r][c] == 1:
                row_str+= "⬛"
            else:
                row_str += "⬜"

print("-" * 50)

time.sleep(0.2)

def solve_basic_maze_animated(grid, start, end):
    rows, col = len(grid), len(grid[0])
    priority_queue = [(0,start)]
    shortest_steps_to_cell = {start: 0}
    visited_cells = set()
    came_from = {}

    while priority_queue:
        current_steps, current_position = heapq.heappop(priority_queue)

        if current_position in visited_cells:
            continue

        animate_search(grid,start,end,visited_cells,priority_queue,came_from,current_position)

        visited_cells.add(current_position)

        if current_position == end:
            path = []
            while current_position in came_from:
                path.append(current_position)
                current_position = came_from[current_position]
            path.append(start)
            path.reverse()
            return path,current_steps

        r, c = current_position

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < col and grid[nr][nc] == 0:
                neighbour_position = (nr, nc)
                calculated_steps = current_steps + 1

                if neighbour_position not in shortest_steps_to_cell or calculated_steps < shortest_steps_to_cell[neighbour_position]:

                    shortest_steps_to_cell[neighbour_position] = calculated_steps
                    came_from[neighbour_position] = current_position
                    heapq.heappush(priority_queue, (calculated_steps, neighbour_position))

    return None, float('inf')

def print_final_path(grid, path, start, end):

    rows, cols = len(grid), len(grid[0])
    path_set = set(path) if path else set()

    for r in range(rows):
        row_str = ""
        for c in range(cols):
            pos = (r, c)
            if pos == start:
                row_str += "🟢 "
            elif pos == end:
                row_str += "🔴 "
            elif pos in path_set:
                row_str += "⭐ "  # Path markers
            elif grid[r][c] == 1:
                row_str += "⬛ "
            else:
                row_str += "⬜ "
        print(row_str)

start_point = (0,0)
end_point = (4, 4)

optimal_route, total_steps = solve_basic_maze_animated(maze_grid, start_point, end_point)

if optimal_route:
    print_final_path(maze_grid, optimal_route, start_point, end_point)
    print(f'\nTotal steps Required: {total_steps}')
else:
    print("\n No path could be found through this maze.")







