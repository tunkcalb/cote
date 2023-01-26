import sys
from collections import deque


# 빈 공간 : 0, 벽: 1, 사과: 2, 뱀: 3

input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())

board = [[1] * (N + 2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N + 2)]

for _ in range(K):
    row, col = map(int, input().rstrip().split())
    board[row][col] = 2

L = int(input().rstrip())

todo = []
for _ in range(L):
    when, direction = input().rstrip().split()

    when = int(when)

    todo.append([when, direction])

time = 0
x, y = 1, 1
direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
# 0: 북, 1: 동, 2: 남, 3: 서
d = 1
snake = deque([[1,1]])
board[1][1] = 3

while 1:
    time += 1
    x += direction[d][0]
    y += direction[d][1]

    if board[x][y] == 2:
        board[x][y] = 3
        snake.append([x,y])

    elif board[x][y] == 0:
        board[x][y] = 3
        snake.append([x,y])
        del_x, del_y = snake.popleft()
        board[del_x][del_y] = 0

    else:
        break


    if len(todo) != 0:
        if todo[0][0] == time:
            if todo[0][1] == "L":
                d = (d - 1) % 4
            if todo[0][1] == "D":
                d = (d + 1) % 4
            del todo[0]

print(time)
