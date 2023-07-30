class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros + self.cents / 100:.2f} eur"


if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1)
    print(e2)