import sys


def solve():
    N = int(input().rstrip())
    cost = [0] + list(map(int, input().rstrip().split()))
    S = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        S[i] = S[i - 1] + cost[i]

    DP = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(2, N + 1):
        for j in range(1, N + 1 - (i - 1)):
            DP[j][j + i - 1] = min(
                [DP[j][j + k] + DP[j + k + 1][j + i - 1] for k in range(i - 1)]
            ) + (S[j + i - 1] - S[j - 1])

    print(DP[1][N])


input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    solve()
