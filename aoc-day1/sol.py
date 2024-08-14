file_path = './input.txt'  # Replace with the actual file path

def get_digits(str1):
    c = []

    for i in str1:
        if i.isdigit():
            c += [int(i)]

    # Note the indentation here
    return c

with open(file_path, 'r') as file:
    lines = file.readlines()

lines = [line.rstrip() for line in lines]

sum = 0
for line in lines:
    digits = get_digits(line)
    sum += digits[0]*10 + digits[-1]

print(sum)

# Now you have the lines of the file stored in the 'lines' variable as a list