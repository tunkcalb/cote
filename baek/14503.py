import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

r, c, d = map(int, input().rstrip().split())
direction = {0:(-1, 0), 1:(0, 1), 2: (1, 0), 3: (0, -1)}
board = [[1] * M] + [[1] + [0] * (N - 2) + [1] for i in range(M - 2)] + [[1] * M]

