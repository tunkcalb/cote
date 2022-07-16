import sys

num = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(num):
    c_list = []
    cabbage = []
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(K):
        X,Y = map(int, sys.stdin.readline().rstrip().split())
        if X <= M-1 and Y <= N-1:
            cabbage.append((X,Y))
    while cabbage:
        connected = [cabbage[0]]
        for c in cabbage:
            if (c[0]-1, c[1]) in connected:
                connected.append(c)
            elif (c[0]+1, c[1]) in connected:
                connected.append(c)
            elif (c[0], c[1]-1) in connected:
                connected.append(c)
            elif (c[0], c[1]+1) in connected:
                 connected.append(c)
        for co in connected:
            cabbage.remove(co)
        c_list.append(connected)
    answer.append(c_list)
for i in range(len(answer)):
    print(len(answer[i]))
