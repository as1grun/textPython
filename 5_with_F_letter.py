def count_words_ending_with_F():
    count = 0
    with open("text1.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.endswith('F') or word.endswith('f'):
                    count += 1
    return count

func_read = count_words_ending_with_F()

print(func_read)