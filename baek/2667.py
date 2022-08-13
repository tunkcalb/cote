def find_house(n, board):
    house = []
    for col in range(n):
        for row in range(n):
            if board[(row, col)] > 0:
                house.append((row, col))
    return house


def generate_candidates(n, board):
    house = find_house(n, board)
    village = []
    while len(house) > 0:
        candidates = [house.pop(0)]

        while True:
            connected = []
            for h in house:
                if (h[0], h[1] - 1) in candidates:
                    connected.append(h)
                elif (h[0], h[1] + 1) in candidates:
                    connected.append(h)
                elif (h[0] - 1, h[1]) in candidates:
                    connected.append(h)
                elif (h[0] + 1, h[1]) in candidates:
                    connected.append(h)

            if len(connected) == 0:
                break

            for c in connected:
                house.remove(c)
            candidates.extend(connected)

        village.append(candidates)

    def key(elem):
        return len(elem)

    village.sort(key=key)
    return village


n = int(input())
board = {}

for col in range(n):
    line = input()
    for row in range(n):
        pos = (row, col)
        board[pos] = int(line[row])
village = generate_candidates(n, board)  # village = [[(int, int), ...], ...]
print(len(village))
for v in village:
    print(len(v))
