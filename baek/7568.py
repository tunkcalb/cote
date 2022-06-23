n = int(input())
build_list = []
for i in range(n):
    x,y = [int(num) for num in input().split()]
    build_list.append((x,y))
build_dic = {build : 1 for build in build_list}

for build in build_list:
    for rank in build_list:
        if build[0] < rank[0] and build[1] < rank[1]:
            build_dic[build] += 1

for build in build_list:
    print(build_dic[build], end = " ")