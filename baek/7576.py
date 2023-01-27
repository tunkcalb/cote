import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
board = []
tomato = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = 0
count = 0
for row in range(N):
    line = list(map(int, input().rstrip().split()))
    board.append(line)
    for col in range(M):
        if line[col] == 0:
            count += 1
        if line[col] == 1:
            tomato.append((col, row, t))
while tomato:
    x, y, t = tomato.popleft()
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if board[ny][nx] == 0:
                board[ny][nx] = 1
                count -= 1
                tomato.append((nx, ny, t + 1))

if count != 0:
    print(-1)
else:
    print(t)
