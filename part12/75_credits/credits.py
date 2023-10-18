from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


if __name__ == "__main__":
    attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
    print(attempt)
    print(attempt.course_name)
    print(attempt.credits)
    print(attempt.grade)
