from collections import deque
import sys


def dfs(result_dfs, relation, V):
    i = V
    if i not in result_dfs:
        result_dfs.append(V)
        print(V, end=' ')
        for y in relation[i]:
            if relation[y] not in result_dfs:
                dfs(result_dfs, relation, y)


def bfs(relation, V):
    visited = []
    queue = deque([V])
    visited.append(V)

    while queue:
        result_bfs = queue.popleft()
        print(result_bfs, end=' ')
        for relation_idx in relation[result_bfs]:
            if relation_idx not in visited:
                visited.append(relation_idx)
                queue.append(relation_idx)


N, M, V = map(int, sys.stdin.readline().rstrip().split())
relation = [[] for _ in range(N+1)]

for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    relation[num1].append(num2)
    relation[num2].append(num1)

for relation_idx in relation:
    relation_idx.sort()

result_dfs = []

dfs(result_dfs, relation, V)
print()
bfs(relation, V)
print()
