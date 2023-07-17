class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60
        self.minutes = self.minutes % 60

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()
