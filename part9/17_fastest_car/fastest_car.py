class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


def fastest_car(cars: list):
    return max([(car.top_speed, car.make) for car in cars])[1]


if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))
