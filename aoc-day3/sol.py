file_path = "./input.txt"
digits = "0123456789"
adj_x = [-1, -1, -1, 1, 1, 1, 0, 0]
adj_y = [-1, 0, 1, 1, 0, -1,-1, 1]
whitelist = digits + '.'

with open(file_path, "r") as file:
    lines = file.readlines()

lines = [line.rstrip() for line in lines]
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

def is_save(i,j):
    for k in range(len(adj_x)):
        adj_i = i + adj_x[k]
        adj_j = j + adj_y[k]
        if adj_i < 0 or adj_i >= len(lines[0]) or adj_j < 0 or adj_j >= len(lines):
            continue
        # print("pair", adj_x[k], adj_y[k])
        # print("Current:", i, j, lines[i][j], "Adjacent:", adj_i, adj_j, lines[adj_i][adj_j])
        if lines[adj_i][adj_j] not in whitelist:
            return False
    return True
    

def bfs(idx, i, j):
    # Check the adjacent cells in the 2D array
    for k in range(i,j):
        if is_save(idx, k) == False:
            return False
            # Do something with the number
    return True

sum = 0
for idx, val in enumerate(lines):
    i = 0
    while len(lines[idx]) - 1 > i:
        while i < len(lines[idx]) - 1 and lines[idx][i] not in digits:
            i += 1
            if i == len(lines[idx]) - 1:
                continue
        j = i
        while j < len(lines[idx]) and lines[idx][j] in digits:
            j += 1
        if i == j:
            continue
        if not bfs(idx, i, j):
            print(int(lines[idx][i:j]))
            sum += int(lines[idx][i:j])
        i = j

print(sum)