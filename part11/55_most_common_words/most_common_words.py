# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    text = clean_text(open(filename, "r").read().replace("\n", " "))
    return {
        word: count_word(text, word)
        for word in text.split(" ")
        if count_word(text, word) >= lower_limit
    }


def count_word(string: str, word: str):
    return sum(1 for w in string.split(" ") if w == word)


def clean_text(string: str):
    return "".join(char for char in string if char.isalpha() or char == " ")


if __name__ == "__main__":
    r1 = most_common_words("comp.txt", 3)
    print(r1)
