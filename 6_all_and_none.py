def count_all_none():
    count_all = 0
    count_none = 0
    with open("text1.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() == "all":
                    count_all += 1
                elif word.lower() == "none":
                    count_none += 1
    return count_all, count_none

print(count_all_none())