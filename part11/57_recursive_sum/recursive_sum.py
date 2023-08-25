def recursive_sum(num: int):
    if num <= 1:
        return num

    return num + recursive_sum(num - 1)


if __name__ == "__main__":
    print(recursive_sum(3))
    print(recursive_sum(5))
    print(recursive_sum(10))
