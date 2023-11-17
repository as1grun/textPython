def count_lines_without_D():
    count = 0
    with open("text1.txt", "r") as file:
        for line in file:
            if not line.startswith('D'):
                count += 1
    return count

readf = count_lines_without_D()

print(readf)