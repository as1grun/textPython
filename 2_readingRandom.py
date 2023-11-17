import random

def read_random_line():
    with open("text1.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines)

print(read_random_line())