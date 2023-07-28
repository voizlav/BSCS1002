# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f"{self.name}, superpowers: {self.superpowers}"


class SuperGroup:
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = None

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def add_member(self, superhero: SuperHero):
        if not self._members:
            self._members = [superhero]
        else:
            self._members.append(superhero)

    def print_group(self):
        print(f"{self._name}, {self._location}")
        print("Members:")
        for superhero in self._members:
            print(superhero)


if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()
