class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        self.seconds += 1
        self.minutes += self.seconds // 60
        self.hours += self.minutes // 60
        self.seconds = self.seconds % 60
        self.minutes = self.minutes % 60
        self.hours = self.hours % 24

    def set(self, hours, minutes):
        self.seconds = 0
        self.minutes = minutes
        self.hours = hours

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    for i in range(6):
        print(clock)
        clock.tick()
    clock.set(12, 5)
    print(clock)
