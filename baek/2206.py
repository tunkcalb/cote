import sys
from collections import deque

def bfs():
    visited = []
    queue = deque([V])
    visited.append(V)

    while queue:
        result_bfs = queue.popleft()
        print(result_bfs, end = ' ')
        for relation_idx in relation[result_bfs]:
            if relation_idx not in visited:
                visited.append(relation_idx)
                queue.append(relation_idx)



input = sys.stdin.readline()
N, M = map(int,sys.stdin.readline().rstrip().split())
board = {}
for row in range(N):
    line = input().rtrip().split()
    for col in range(M):
        pos = (row, col)
        board[pos] = line[col]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque()
