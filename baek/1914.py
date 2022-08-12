import sys

def hanoiTop_print(n, x, y):
    if n > 1:
        hanoiTop_print(n-1, x,6 - x - y)

    print(x, y)

    if n > 1:
        hanoiTop_print(n-1, 6 - x - y, y)

input = sys.stdin.readline
n = int(input().rstrip())
print(2 ** n - 1)

if n <= 20:
    hanoiTop_print(n, 1, 3)
