class Course:
    def __init__(self, name: str, grade: int, credit: int):
        self.__name = name
        self.__grade = grade
        self.__credit = credit

    @property
    def name(self):
        return self.__name

    @property
    def credit(self):
        return self.__credit

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade: int):
        if self.__grade > grade:
            raise ValueError("grade cannot be lowered")
        self.__grade = grade

    def __str__(self):
        return f"{self.__name} ({self.__credit} cr) grade {self.__grade}"


if __name__ == "__main__":
    c1 = Course("ITP", 1, 5)
    print(c1)
    c1.grade = 3
    print(c1)
