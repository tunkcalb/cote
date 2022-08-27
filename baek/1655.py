import sys
import heapq

input = sys.stdin.readline

def use_list():
    N = int(input().rstrip())

    num = [int(input().rstrip())]
    odd = True
    mid_idx = 0
    length = 1
    print(num[0])

    for i in range(N-1):
        odd = not odd
        new_num = int(input().rstrip())

        if num[mid_idx] > new_num:
            for j in range(mid_idx):
                if num[j] > new_num:
                    num.insert(j, new_num)
                    if odd == True:
                        mid_idx += 1
                        length += 1
            else:
                num.insert(mid_idx, new_num)
                if odd == True:
                    mid_idx += 1
                    length += 1

        elif num[mid_idx] < new_num:
            for j in range(length - mid_idx):
                if num[length - 1 - j] < new_num:
                    num.insert(length - j, new_num)
                    if odd == True:
                        mid_idx += 1
                        length += 1
            else:
                num.insert(mid_idx + 1, new_num)
                if odd == True:
                    mid_idx += 1
                    length += 1

        else:
            num.insert(mid_idx + 1, new_num)
            if odd == True:
                mid_idx += 1
                length += 1

            else:
                length += 1

        print(num[mid_idx])

def use_heap():
    N = int(input().rstrip())

    low_heap = []
    high_heap = []

    for i in range(N):
        num = int(input().rstrip())

        if len(low_heap) == len(high_heap):
            heapq.heappush(low_heap, -num)

        else:
            heapq.heappush(high_heap, num)

        if high_heap and low_heap[0] * -1 > high_heap[0]:
            high_value = heapq.heappop(low_heap)
            low_value = heapq.heappop(high_heap)

            heapq.heappush(low_heap, low_value * -1)
            heapq.heappush(high_heap, high_value * -1)

        print(low_heap[0] * -1)

use_heap()
