import sys

input = sys.stdin.readline

def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True


def queen(x, n):
    global count
    if x == n:
        count += 1
    else:
        for i in range(n):
            board[x] = i
            if check(x):
                queen(x+1, n)

count = 0
n = int(input().rstrip())
board = [0] * n
queen(0, n)
print(count)
