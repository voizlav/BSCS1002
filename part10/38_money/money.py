class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __money(self):
        return self.euros + self.cents / 100

    def __str__(self):
        return f"{self.__money():.2f} eur"

    def __eq__(self, other: 'Money'):
        return self.__money() == other.__money()


if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)
