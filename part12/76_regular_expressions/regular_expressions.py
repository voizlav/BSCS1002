import re


def is_dotw(my_string: str):
    pattern = "^(mon|tue|wed|thu|fri|sat|sun)$"
    return True if re.search(pattern, my_string, re.IGNORECASE) else False


def all_vowels(my_string: str):
    pattern = "^[aeiou]+$"
    return True if re.search(pattern, my_string, re.IGNORECASE) else False


def time_of_day(my_string: str):
    pattern = "^([01][0-9]|2[0-3])(:[0-5][0-9]){2}$"
    return True if re.search(pattern, my_string) else False


if __name__ == "__main__":
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))
    print(is_dotw("Sunny"))

    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
