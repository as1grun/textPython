def word_frequency():
    frequency = {}
    with open("text1.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1
    return frequency

print(word_frequency())