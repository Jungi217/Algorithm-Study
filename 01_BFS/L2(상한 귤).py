import sys
from collections import deque

n, k = map(int, input().split())
dist = [[-2] * n for _ in range(n)]

q = deque()
# 0: 빈칸, 1: 정상 귤, 2: 상한 귤
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(n):
        if row[j] == 2:
            dist[i][j] = 0
            q.append((i, j))
        elif row[j] == 0:
            dist[i][j] = -1

def bfs():
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1 and dist[nx][ny] == -2:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

bfs()

for row in dist:
    print(*row)