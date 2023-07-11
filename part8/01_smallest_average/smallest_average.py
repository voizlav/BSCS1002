def smallest_average(p1: dict, p2: dict, p3: dict) -> dict:
    average, person = float("inf"), {}
    for p in [p1, p2, p3]:
        nums = [num for num in p.values() if isinstance(num, int)]
        if average > sum(nums) / len(nums):
            average, person = sum(nums) / len(nums), p
    return person


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))
