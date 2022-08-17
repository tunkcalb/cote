import sys
import math

input = sys.stdin.readline

N = int(input())
num = []
answer = []
gcd = 0
for i in range(N):
    num.append(int(input()))
    if i == 1:
        gcd = abs(num[1] - num[0])
    gcd = math.gcd(abs(num[i] - num[i - 1]), gcd)
gcd_sqrt = int(gcd ** 0.5)
for i in range(2, gcd_sqrt + 1):
    if gcd % i == 0:
        answer.append(i)
        answer.append(gcd // i)
answer.append(gcd)
answer = list(set(answer))
answer.sort()
for i in answer:
    print(i, end = ' ')
