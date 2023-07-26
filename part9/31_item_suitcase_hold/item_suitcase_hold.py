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
    pass


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")
