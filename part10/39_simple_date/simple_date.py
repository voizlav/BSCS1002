

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day if day > 0 else 1
        self.__month = month if month > 0 else 1
        self.__year = year if year > 0 else 1
        self.__update()

    def __update(self):
        total_days = self.__total_days()
        self.__year = 1 + (total_days // 360)
        total_days %= 360
        self.__month = 1 + (total_days // 30)
        self.__day = total_days % 30

    def __total_days(self):
        return (self.__year - 1) * 360 + (self.__month - 1) * 30 + self.__day

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

    def __add__(self, other: int):
        return SimpleDate(self.__day + other, self.__month, self.__year)

    def __sub__(self, other: 'SimpleDate'):
        return abs(self.__total_days() - other.__total_days())


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)
    print(d1 + 3)
    print(d2 + 400)
