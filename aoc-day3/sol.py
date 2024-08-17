file_path = "./input.txt"
digits = "0123456789"

with open(file_path, "r") as file:
    lines = file.readlines()

lines = [line.rstrip() for line in lines]


def bfs(idx, i, j):
    # Check the adjacent cells in the 2D array
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x >= 0 and x < len(lines[idx]) and y >= 0 and y < len(lines):
                if lines[y][x] not in digits:
                    print(f"Adjacent cell at ({x}, {y}) is a special character.")
                else:
                    print(f"Adjacent cell at ({x}, {y}) is not a special character.")


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
        print(idx, i, j, lines[idx][i:j])
        bfs(idx, i, j - 1)
        i = j
