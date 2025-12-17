import sys
from collections import deque

n = int(input())
q = deque()

def bfs():
    visited = {n: 0}
    q.append(n)
    # q = deque([n])도 가능함. 주의할 점은 deque(n)으로 할 경우 오류 발생(deque의 작동원리 참고)
    while q:
        num = q.popleft()
        cnt = visited[num]
        if num == 1:
            print(cnt)
            return

        next_nums = []
        if num % 3 == 0:
            next_nums.append(num // 3)
        if num % 2 == 0:
            next_nums.append(num // 2)
        next_nums.append(num - 1)
        next_nums.append(num + 1)

        for next_num in next_nums:
            if 1 <= next_num <= n + 1 and next_num not in visited:
                q.append(next_num)
                visited[next_num] = cnt + 1

bfs()