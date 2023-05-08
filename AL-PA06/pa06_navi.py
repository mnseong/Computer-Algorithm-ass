import heapq
import sys

input = sys.stdin.readline


# 맨해튼 거리를 계산하는 함수
def manhattan_distance(coord1, coord2):
    distance = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    return distance


# A* Algorithm
def astar_algorithm(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    start_node = (manhattan_distance(start, goal), start, 0)
    heap = [start_node]
    visited = set()

    while heap:
        _, current, cost = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return cost

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_row, next_col = current[0] + dr, current[1] + dc
            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == 1:
                next_node = (manhattan_distance((next_row, next_col), goal) + cost + 1, (next_row, next_col), cost + 1)
                heapq.heappush(heap, next_node)
    return -1


# 장애물 지역을 0으로 바꾸어 주는 함수
def set_rectangle_to_zero(grid, a, b, c, d):
    min_row, max_row = min(a, c), max(a, c)
    min_col, max_col = min(b, d), max(b, d)

    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            grid[row][col] = 0


m, n = map(int, input().split())
total_map = [[1] * (n + 1) for _ in range(m + 1)]
zero_num = int(input())
zero_cells = [list(map(int, input().split())) for i in range(zero_num)]

for i in range(zero_num):
    _, tx, ty = map(int, zero_cells[i])
    total_map[tx][ty] = 0

start = tuple(map(int, list(map(str, input().split()))[1:]))
end = tuple(map(int, list(map(str, input().split()))[1:]))
_, num_obstacle = map(str, input().split())
num_obstacle = int(num_obstacle)
obstacles = [list(map(int, input().split())) for i in range(num_obstacle)]

for i in range(len(obstacles)):
    set_rectangle_to_zero(total_map, obstacles[i][0], obstacles[i][1], obstacles[i][2], obstacles[i][3])

path = astar_algorithm(total_map, start, end) * 3
print(path)
