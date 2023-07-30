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

    def __ne__(self, other: 'Money'):
        return self.__money() != other.__money()

    def __lt__(self, other: 'Money'):
        return self.__money() < other.__money()

    def __gt__(self, other: 'Money'):
        return self.__money() > other.__money()

if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
