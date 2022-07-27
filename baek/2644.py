import sys

def p_list(p):
    p_list2 = []
    i = p
    while True:
        if i == None:
            break
        p_list2.append(i)
        i = family.get(i)
    return p_list2

input = sys.stdin.readline

n = int(input().rstrip())
p1, p2 = map(int, input().rstrip().split())
m = int(input().rstrip())
family = {}

for i in range(m):
    x, y = map(int, input().rstrip().split())
    family[y] = x

p1_list = p_list(p1)
p2_list = p_list(p2)
p3 = set(p1_list).intersection(set(p2_list))
if p3 == set():
    print(-1)
else:
    if len(p3) > 1:
        p3 = list(p3)[0]
        print(p1_list.index(p3) + p2_list.index(p3))
    else:
        p3=p3.pop()
        print(p1_list.index(p3) + p2_list.index(p3))
