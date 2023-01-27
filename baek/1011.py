import sys

input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    start, end = map(int, input().rstrip().split())

    distance = end - start
    n = 0
    while distance > n * (n + 1):
        n += 1

    if distance > n**2:
        print(2 * n)
    else:
        print(2 * n - 1)
