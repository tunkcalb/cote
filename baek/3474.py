import sys


T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    result = 0
    while N >= 1 :
        result += N//5
        N /= 5
    print(int(result))
