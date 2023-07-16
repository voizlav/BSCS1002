class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self) -> int:
        return len(self.numbers)

    def get_sum(self) -> int:
        return 0 if not self.numbers else sum(self.numbers)

    def average(self) -> int:
        return 0 if not self.numbers else self.get_sum() / self.count_numbers()


def main():
    stats_all = NumberStats()
    stats_even = NumberStats()
    stats_odd = NumberStats()

    print("Please type in integer numbers:")
    while True:
        try:
            get_input = int(input())
        except ValueError:
            continue
        if get_input == -1:
            break
        if get_input % 2 == 0:
            stats_even.add_number(get_input)
        else:
            stats_odd.add_number(get_input)
        stats_all.add_number(get_input)

    print("Sum of numbers:", stats_all.get_sum())
    print("Mean of numbers:", stats_all.average())
    print("Sum of even numbers:", stats_even.get_sum())
    print("Sum of odd numbers:", stats_odd.get_sum())


main()
