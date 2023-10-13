from random import choices


def word_generator(characters: str, length: int, amount: int):
    return ("".join(choices(characters, k=length)) for _ in range(amount))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
