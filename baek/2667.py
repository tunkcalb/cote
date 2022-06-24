def find_house(n, board):
    house = []
    for col in range(n):
        for row in range(n):
            if board[(row,col)] >0 :
                house.append((row,col))
    return house

def generate_candidates(n, board):
    house = find_house(n, board)
    village = []
    for i in range(len(house)):
        if i > len(house):
            return
        candidates = []
        house_idx = 0
        candidates.append(house[0])
        house.pop(0)
        
        while True:
            if (house[house_idx][0], house[house_idx][1]-1) in candidates:
                candidates.append(house[house_idx])
                house.pop[house_idx]
                return True
            elif (house[house_idx][0], house[house_idx][1]+1) in candidates:
                candidates.append(house[house_idx])
                house.pop[house_idx]
                return True
            elif (house[house_idx][0]-1, house[house_idx][1]) in candidates:
                candidates.append(house[house_idx])
                house.pop[house_idx]
                return True
            elif (house[house_idx][0]+1, house[house_idx][1]) in candidates:
                candidates.append(house[house_idx])
                house.pop[house_idx]
                return True
            else:
                house_idx += 1
            if house_idx > len(house):
                return False
        village.append(candidates)
    return village


n = int(input())
board = {}

for col in range(n):
    line = input()
    for row in range(n):
        pos = (row, col)
        board[pos] = int(line[row])
village = generate_candidates(n, board)
print(len(village))
for i in range(village):
    print(len(village[i]))