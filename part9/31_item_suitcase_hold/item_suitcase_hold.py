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

    def __total_weight(self):
        return sum(item.weight() for item in self.__items)

    def add_item(self, item: Item):
        if self.__maximum_weight > self.__total_weight() + item.weight():
            self.__items.append(item)

    def __str__(self):
        return f"{len(self.__items)} {'item' if len(self.__items) == 1 else 'items'} ({self.__total_weight()} kg)"


class CargoHold:
    pass


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)
