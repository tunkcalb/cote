import sys


input = sys.stdin.readline

N = int(input().rstrip())

efficiency = []
for i in range(N):
    T, S = map(int, input().rstrip().split())
    efficiency.append([T / S , i + 1])
efficiency.sort()

for e in efficiency:
    print(e[1], end = " ")
