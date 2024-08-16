from functools import reduce

file_path = "./input.txt"


with open(file_path, "r") as file:
    lines = file.readlines()

lines = [line.rstrip() for line in lines]

sum = 0
for line in lines:
    first, rest = line.split(":")
    game_id = int(first.split(" ")[1])
    bags = rest.split(";")
    set_num = [0, 0, 0]
    for bag in bags:
        bag = bag.strip()
        mini_bags = bag.split(",")
        for mini_bag in mini_bags:
            mini_bag = mini_bag.strip()
            if mini_bag == "":
                continue
            count, color = mini_bag.split(" ", 1)
            count = int(count)
            print(count, color)
            if color == "red":
                set_num[0] = max(set_num[0], count)
            if color == "green":
                set_num[1] = max(set_num[1], count)
            if color == "blue":
                set_num[2] = max(set_num[2], count)
    sum += reduce(lambda x, y: x * y, set_num, 1)
    print(game_id, bags)
print(sum)
