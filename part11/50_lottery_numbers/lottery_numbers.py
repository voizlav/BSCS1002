class LotteryNumbers:
    def __init__(self, week: int, numbers: []):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, numbers: []):
        return len([num for num in numbers if num in self.numbers])

    def hits_in_place(self, numbers: []):
        return [num if num in self.numbers else -1 for num in numbers]


if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
    my_numbers = [1, 4, 7, 11, 13, 19, 24]
    print(week5.number_of_hits(my_numbers))

    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers = [1, 4, 7, 10, 11, 20, 30]
    print(week8.hits_in_place(my_numbers))
