import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
    
def bfs(x, y):
    board[x][y] = 0
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] ==1:
                board[nx][ny] = 0
                queue.append([nx, ny])

while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    board = []
    count = 0
    for _ in range(h):
        board.append(list(map(int, input().rstrip().split())))
    for j in range(w):
        for i in range(h):
            if board[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
