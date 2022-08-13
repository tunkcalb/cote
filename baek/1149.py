import sys


N = int(sys.stdin.readline().rstrip())

cost = [[] for i in range(N)]
for i in range(N):
    if i == 0:
        rgb = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(len(rgb)):
            cost[i].append(rgb[j])
    else:
        rgb = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(len(rgb)):
            if j == 0:
                cost[i].append(rgb[j] + min(cost[i-1][1], cost[i-1][2]))
            elif j == 1:
                cost[i].append(rgb[j] + min(cost[i-1][0], cost[i-1][2]))
            else:
                cost[i].append(rgb[j] + min(cost[i-1][0], cost[i-1][1]))
print(min(cost[N-1]))
