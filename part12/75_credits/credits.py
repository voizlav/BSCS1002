from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(credits: list):
    return reduce(lambda total, attempt: total + attempt.credits, credits, 0)


def sum_of_passed_credits(credits: list):
    credits = filter(lambda attempt: attempt.grade > 0, credits)
    return reduce(lambda total, attempt: total + attempt.credits, credits, 0)


def average(grades: list):
    grades = list(filter(lambda attempt: attempt.grade > 0, grades))
    return reduce(lambda total, attempt: total + attempt.grade, grades, 0) / len(grades)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)

    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    ag = average([s1, s2, s3])
    print(ag)
