class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, maximum_weight: int):
        self.__maximum_weight = maximum_weight
        self.__items = []

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        if not self.__items:
            return None
        return max([(item.weight(), item) for item in self.__items])[1]

    def add_item(self, item: Item):
        if self.__maximum_weight > self.weight() + item.weight():
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def __str__(self):
        return f"{len(self.__items)} {'item' if len(self.__items) == 1 else 'items'} ({self.weight()} kg)"


class CargoHold:
    def __init__(self, maximum_weight: int):
        self.__maximum_weight = maximum_weight
        self.__suitcases = []

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.__suitcases)

    def space(self):
        return self.__maximum_weight - self.weight()

    def add_suitcase(self, suitcase: Suitcase):
        if self.__maximum_weight > self.weight() + suitcase.weight():
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        return f"{len(self.__suitcases)} {'suitcase' if len(self.__suitcases) == 1 else 'suitcases'}, space for {self.space()} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
