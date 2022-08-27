import sys

input = sys.stdin.readline

m = int(input().rstrip())
f = [0] + list(map(int, input().rstrip().split()))

DP = [[f[i]] for i in range(m + 1)]
for j in range(1, 19):
    for i in range(1, m + 1):
        DP[i].append(DP[DP[i][j - 1]][j - 1])

Q = int(input().rstrip())
for _ in range(Q):
    n, x = map(int, input().rstrip().split())

    for i in range(18, -1, -1):
        if n >= 1 << i:
            n -= 1 << i
            x = DP[x][i]
    print(x)
