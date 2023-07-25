class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        count = {number: my_list.count(number) for number in my_list}
        return max([(count[number], number) for number in count])[1]

    @classmethod
    def doubles(cls, my_list: list):
        count = {number: my_list.count(number) for number in my_list}
        return sum(1 for number in count if count[number] > 1)


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
