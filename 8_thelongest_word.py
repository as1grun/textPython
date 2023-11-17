def longest_word():
    longest = ""
    with open("text1.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > len(longest):
                    longest = word
    return longest

print(longest_word())