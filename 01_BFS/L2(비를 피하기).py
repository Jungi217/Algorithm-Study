from collections import deque
n, h, m = map(int, input().split())
# 0: 이동 가능, 1:이동 불가, 2: 사람, 3: 비 안전 공간
grid = [list(map(int, input().split())) for _ in range(n)]

# bfs 진행 시 칸 방문 확인을 위해 필요
visited = [
    [False] * n
    for _ in range(n)
]

distance = [[-1 for _ in range(n)] for _ in range(n)]
# 비를 피할 수 있는 공간 저장
safety_pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            safety_pos.append((i, j))

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 1

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

q = deque()
for x, y in safety_pos:
    visited[x][y] = True
    q.append((x, y))
    distance[x][y] = 0

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            print(distance[i][j], end=" ")
        else:
            print(0, end=" ")
    print()