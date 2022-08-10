import sys
from collections import deque

input = sys.stdin.readline

def bfs(s_x, s_y, d_x, d_y):
    count = 0
    queue = deque()
    queue.append([s_x, s_y, count])
    board[s_x][s_y] = 1
    
    while queue:
        x, y, count = queue.popleft()
        if x == d_x and y == d_y:
            print(count)
            break
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and board[nx][ny] == 0:
                queue.append([nx, ny, count+1])
                board[nx][ny] = 1

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
N = int(input().rstrip())
for i in range(N):
    L = int(input().rstrip())
    board = [[0]*L for j in range(L)]
    s_x, s_y = map(int, input().rstrip().split())
    d_x, d_y = map(int, input().rstrip().split())

    if s_x == d_x and s_y == d_y:
        print(0)
        continue
    bfs(s_x, s_y, d_x, d_y)
