class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return False if self.people else True

    def shortest(self):
        if self.is_empty():
            return None
        return min([(person.height, person) for person in self.people])[1]

    def remove_shortest(self):
        if person := self.shortest():
            self.people.remove(person)
        return person

    def print_contents(self):
        print(f"There are {len(self.people)} persons in the room, ", end="")
        print(f"and their combined height is {sum(p.height for p in self.people)} cm")
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")
