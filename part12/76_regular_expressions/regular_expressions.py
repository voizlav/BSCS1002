import re


def is_dotw(my_string: str):
    pattern = "^(mon|tue|wed|thu|fri|sat|sun)$"
    if re.search(pattern, my_string, re.IGNORECASE):
        return True
    return False


def all_vowels(my_string: str):
    pattern = "^[aeiou]+$"
    if re.search(pattern, my_string, re.IGNORECASE):
        return True
    return False


if __name__ == "__main__":
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))
    print(is_dotw("Sunny"))

    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))
