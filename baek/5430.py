import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())

for i in range(N):
    stop = False
    function = input().rstrip()
    length = int(input().rstrip())
    li = input().rstrip()
    line = deque(li[1:-1].split(","))
    function = function.replace("RR", "")
    R = 1
    if length == 0:
        line = deque()
    for j in function:
        if j == "R":
            R *= -1
        else:
            if len(line) == 0:
                print("error")
                stop = True
                break
            else:
                if R == 1:
                    line.popleft()
                else:
                    line.pop()

    if stop == True:
        continue
    else:
        if R == 1:
            print("[" + ",".join(line) + "]")
        else:
            line.reverse()
            print("[" + ",".join(line) + "]")
