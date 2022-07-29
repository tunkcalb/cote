import sys
from collections import deque

def dfs(x, y, current):
    global Max
    if Max < current:
        Max = current

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny <= C and not board[nx][ny] in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, current + 1)
            visited.remove(board[nx][ny])

def bfs():
    Max = 1
    queue = set([(0,0,board[0][0])])

    while queue:
        x, y, visited = queue.pop()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in visited:
                next_visited = visited + board[nx][ny]
                queue.add((nx, ny, next_visited))
                Max = max(Max, len(next_visited))
    return Max

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
board = []
Max = 1
for _ in range(R):
    board.append(input().rstrip())
#visited = set()
#visited.add(board[0][0])
visited = []
print(bfs())
