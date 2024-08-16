file_path = "./input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

lines = [line.rstrip() for line in lines]

sum = 0
for line in lines:
    first, rest = line.split(":")
    game_id = int(first.split(" ")[1])
    bags = rest.split(";")
    is_legit = True
    for bag in bags:
        bag = bag.strip()
        if is_legit == False:
            break
        mini_bags = bag.split(",")
        for mini_bag in mini_bags:
            mini_bag = mini_bag.strip()
            if mini_bag == "":
                continue
            count, color = mini_bag.split(" ", 1)
            count = int(count)
            print(count, color)
            if color == "red" and count > 12:
                is_legit = False
                break
            if color == "green" and count > 13:
                is_legit = False
                break
            if color == "blue" and count > 14:
                is_legit = False
                break
    if is_legit:
        sum += game_id
    print(game_id, bags)
print(sum)
