import sys
from itertools import combinations, product


def wall_construct(empty, wall_num, board):
    for wall_comb in combinations(empty, wall_num):
        for x_w, y_w in wall_comb:
            board[(x_w, y_w)] = 1
        virus(board)
        for x_w, y_w in wall_comb:
            board[(x_w, y_w)] = 0
        for row, col in product(range(N), range(M)):
            if board[(row, col)] == 3:
                board[(row, col)] = 0


def virus(board_wall):

    # 바이러스 위치
    virus = [(n, m) for n in range(N)
             for m in range(M) if board_wall[(n, m)] == 2]

    while virus:
        x, y = virus.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and board_wall[(nx, ny)] == 0:
                board_wall[(nx, ny)] = 3
                virus.append((nx, ny))
    safezone(board_wall)


def safezone(board_wall):
    global answer
    safezone_count = 0

    for key in board_wall:
        if board_wall[key] == 0:
            safezone_count += 1
        answer = max(answer, safezone_count)


board = {}
N, M = map(int, sys.stdin.readline().rstrip().split())

for row in range(N):
    line = sys.stdin.readline().rstrip().split()
    for col in range(M):
        pos = (row, col)
        board[pos] = int(line[col])

empty = [(n, m) for n in range(N) for m in range(M) if board[(n, m)] == 0]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
wall_num = 3


wall_construct(empty, wall_num, board)
print(answer)
