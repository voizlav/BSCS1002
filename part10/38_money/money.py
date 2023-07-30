class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __money(self):
        return self.__euros + self.__cents / 100

    def __str__(self):
        return f"{self.__money():.2f} eur"

    def __eq__(self, other: 'Money'):
        return self.__money() == other.__money()

    def __ne__(self, other: 'Money'):
        return self.__money() != other.__money()

    def __lt__(self, other: 'Money'):
        return self.__money() < other.__money()

    def __gt__(self, other: 'Money'):
        return self.__money() > other.__money()

    def __add__(self, other: 'Money'):
        return Money(self.__euros + other.__euros, self.__cents + other.__cents)

    def __sub__(self, other: 'Money'):
        if self < other:
            raise ValueError("a negative result is not allowed")
        return Money(self.__euros - other.__euros, self.__cents - other.__cents)


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2 - e1
