n = int(input())
build_list = []

for i in range(n):
    x, y = [int(num) for num in input().split()]
    build_list.append((x, y))

for build in build_list:
    count = 1
    for rank in build_list:
        if build[0] < rank[0] and build[1] < rank[1]:
            count += 1
    print(count, end=" ")
