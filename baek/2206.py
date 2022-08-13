import sys
from collections import deque


def bfs(start_x, start_y, crash):
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((start_x, start_y, crash))
    visited[start_x][start_y][crash] = 1

    while queue:
        x, y, crash = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][crash]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[(nx, ny)] == 1 and crash == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                elif board[(nx, ny)] == 0 and visited[nx][ny][crash] == 0:
                    visited[nx][ny][crash] = visited[x][y][crash] + 1
                    queue.append((nx, ny, crash))
    return -1


input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
board = {}
for row in range(N):
    line = input().rstrip()
    for col in range(M):
        pos = (row, col)
        board[pos] = int(line[col])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0, 0))
