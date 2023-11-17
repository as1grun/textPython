def count_uppercase_chars():
    count = 0
    with open("text1.txt", "r") as file:
        for line in file:
            for char in line:
                if char.isupper():
                    count += 1
    return count

c_upper_char = count_uppercase_chars()

print(c_upper_char)