import sys

num = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(num):
    c_list = []
    cabbage = []
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        if X <= M - 1 and Y <= N - 1:
            cabbage.append((X, Y))
    while cabbage:
        connected = [cabbage.pop(0)]
        fresh_cabbage = []
        while True:
            for c in cabbage:
                if (c[0] - 1, c[1]) in connected:
                    fresh_cabbage.append(c)
                elif (c[0] + 1, c[1]) in connected:
                    fresh_cabbage.append(c)
                elif (c[0], c[1] - 1) in connected:
                    fresh_cabbage.append(c)
                elif (c[0], c[1] + 1) in connected:
                    fresh_cabbage.append(c)
            if len(fresh_cabbage) == 0:
                break
            for f in fresh_cabbage:
                cabbage.remove(f)
            connected.extend(fresh_cabbage)
            fresh_cabbage.clear()

        c_list.append(connected)
    answer.append(c_list)
for i in range(len(answer)):
    print(len(answer[i]))
