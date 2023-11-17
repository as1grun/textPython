def count_chars():
    with open("text1.txt", "r") as file:
        content = file.read()

    a_count = content.lower().count("a")
    b_count = content.lower().count("b")

    return a_count, b_count

print(count_chars())