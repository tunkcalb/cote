import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solve(node):
    visited[node] = True
    for next_node in tree[node]:
        if not visited[next_node]:
            solve(next_node)
            dp[node][0] += dp[next_node][1]
            dp[node][1] += min(dp[next_node][0], dp[next_node][1])


n = int(input().rstrip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 1] for _ in range(n + 1)]
visited = [False] * (n + 1)
root = 1

solve(root)
print(min(dp[root]))
