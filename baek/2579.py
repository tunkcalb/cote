import sys


def solve(stair, n):
    dp = []
    dp.append(stair[0])
    dp.append(max(dp[0] + stair[1], stair[1]))
    dp.append(max(stair[1] + stair[2], dp[0] + stair[2]))

    for i in range(3, n):
        dp.append(max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2]))
    print(dp[-1])


stair = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    stair.append(int(sys.stdin.readline().rstrip()))

if n == 1:
    print(stair[0])
    exit()
elif n == 2:
    print(max(stair[0] + stair[1], stair[1]))
    exit()


solve(stair, n)
