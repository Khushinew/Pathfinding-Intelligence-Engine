import heapq
import os
import time

traffic_map = [
    [3, -1, 1, 3, 10],
    [1, -1, -1, -1, 3],
    [1, 1, 1, 1, 1]
]


def animate_traffic_search(grid, start, end, visited, active_queue, current_pos):
    os.system("cls" if os.name == "nt" else "clear")

    rows, cols = len(grid), len(grid[0])
    queue_coords = {pos for _, pos in active_queue}

    print("Dijkstra's Traffic Router Animation .......\n")

    for r in range(rows):
        row_str = ""

        for c in range(cols):
            pos = (r, c)
            val = grid[r][c]

            if pos == start:
                row_str += "🟢 "
            elif pos == end:
                row_str += "🔴 "
            elif pos == current_pos:
                row_str += "🎯 "
            elif pos in queue_coords:
                row_str += "🟡 "
            elif pos in visited:
                row_str += "🔍 "
            elif val == -1:
                row_str += "🚧 "
            elif val == 10:
                row_str += "🚗 "
            elif val == 3:
                row_str += "🚙 "
            else:
                row_str += "🛣️ "

        print(row_str)

    print("\nLegend: 🟢 Start | 🔴 Exit | 🎯 Active | 🟡 In Queue | 🔍 Visited")
    print("        🛣️ Highway (1) | 🚙 City (3) | 🚗 Traffic (10) | 🚧 Closed (-1)")
    print("-" * 50)

    time.sleep(0.3)


def solve_traffic_routing(grid, start, end):

    rows, cols = len(grid), len(grid[0])

    priority_queue = [(0, start)]
    visited_intersections = set()
    came_from = {}
    fastest_time_to_intersection = {start: 0}

    while priority_queue:

        current_time, current_position = heapq.heappop(priority_queue)

        if current_position in visited_intersections:
            continue

        animate_traffic_search(
            grid,
            start,
            end,
            visited_intersections,
            priority_queue,
            current_position
        )

        visited_intersections.add(current_position)

        if current_position == end:

            path = []

            while current_position in came_from:
                path.append(current_position)
                current_position = came_from[current_position]

            path.append(start)
            path.reverse()

            return path, current_time

        r, c = current_position

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:

                neighbor_position = (nr, nc)

                road_weight = grid[nr][nc]
                calculated_time = current_time + road_weight

                if (
                    neighbor_position not in fastest_time_to_intersection
                    or calculated_time < fastest_time_to_intersection[neighbor_position]
                ):

                    fastest_time_to_intersection[neighbor_position] = calculated_time

                    came_from[neighbor_position] = current_position

                    heapq.heappush(
                        priority_queue,
                        (calculated_time, neighbor_position)
                    )

    return None, float('inf')


def print_final_route(grid, path, start, end):

    rows, cols = len(grid), len(grid[0])
    path_set = set(path) if path else set()

    print("\n🎉 OPTIMAL ROUTE CALCULATED (FASTEST TIME):\n")

    for r in range(rows):

        row_str = ""

        for c in range(cols):

            pos = (r, c)

            if pos == start:
                row_str += "🟢 "
            elif pos == end:
                row_str += "🔴 "
            elif pos in path_set:
                row_str += "⭐ "
            elif grid[r][c] == -1:
                row_str += "🚧 "
            elif grid[r][c] == 10:
                row_str += "🚗 "
            elif grid[r][c] == 3:
                row_str += "🚙 "
            else:
                row_str += "🛣️ "

        print(row_str)


start_point = (0, 0)
end_point = (2, 4)

fastest_route, total_time = solve_traffic_routing(
    traffic_map,
    start_point,
    end_point
)

if fastest_route:

    print_final_route(
        traffic_map,
        fastest_route,
        start_point,
        end_point
    )

    print(f'⏱️ Total Estimated Travel Time: {total_time} minutes')

else:

    print("\n❌ All roads to the destination are completely blocked by closures.")