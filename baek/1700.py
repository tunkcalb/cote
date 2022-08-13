import sys


def schedule():

    plugs = []
    count = 0

    for i in range(K):
        if line[i] in plugs:
            continue
        if len(plugs) < N:
            plugs.append(line[i])
            continue

        temp = 0
        far_one = 0
        for plug in plugs:
            if plug not in line[i:]:
                temp = plug
                break
            elif line[i:].index(plug) > far_one:
                far_one = line[i:].index(plug)
                temp = plug

        plugs[plugs.index(temp)] = line[i]
        count += 1

    return count


input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
line = list(map(int, input().rstrip().split()))

print(schedule())
