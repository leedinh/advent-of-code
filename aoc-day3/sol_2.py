file_path = "./input.txt"
digits = "0123456789"
adj_x = [-1, -1, -1, 1, 1, 1, 0, 0]
adj_y = [-1, 0, 1, 1, 0, -1,-1, 1]
whitelist = digits + '.'

with open(file_path, "r") as file:
    lines = file.readlines()

lines = [line.rstrip() for line in lines]
map = {}
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

def is_gear(i,j):
    for k in range(len(adj_x)):
        adj_i = i + adj_x[k]
        adj_j = j + adj_y[k]
        if adj_i < 0 or adj_i >= len(lines[0]) or adj_j < 0 or adj_j >= len(lines):
            continue
        # print("pair", adj_x[k], adj_y[k])
        # print("Current:", i, j, lines[i][j], "Adjacent:", adj_i, adj_j, lines[adj_i][adj_j])
        if lines[adj_i][adj_j] == "*":
            return (True, adj_j*len(lines[0]) + adj_i)
    return (False, -1)
    

def bfs(idx, i, j):
    # Check the adjacent cells in the 2D array
    for k in range(i,j):
        res = is_gear(idx, k)
        if res[0]:
            return (True, res[1])
            # Do something with the number
    return (False, -1)

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
        res=  bfs(idx, i, j)
        if res[0]:
            print(int(lines[idx][i:j]))
            if res[1] in map:
                sum += map[res[1]] * int(lines[idx][i:j])
            else:
                map[res[1]] = int(lines[idx][i:j])
        i = j
print(sum)
