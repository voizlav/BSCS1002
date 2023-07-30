class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __total_days(self):
        return self.__day + self.__month * 30 + self.__year * 365

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __eq__(self, other: 'SimpleDate'):
        return self.__total_days() == other.__total_days()

    def __ne__(self, other: 'SimpleDate'):
        return self.__total_days() != other.__total_days()

    def __gt__(self, other: 'SimpleDate'):
        return self.__total_days() > other.__total_days()

    def __lt__(self, other: 'SimpleDate'):
        return self.__total_days() < other.__total_days()


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)
