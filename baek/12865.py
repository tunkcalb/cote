import sys

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
dp = []
item = []

for _ in range(N):
    item.append(list(map(int, input().rstrip().split())))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int, item[i-1])
    for j in range(1, K+1):
        if weight <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
