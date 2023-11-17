def correct_chars():
    with open("text1.txt", "r") as file:
        content = file.read()
        content = content.lower()

    corrected_content = content.replace("b", "j")

    with open("text1.txt", "w") as file:
        file.write(corrected_content)

    return corrected_content

print(correct_chars())
