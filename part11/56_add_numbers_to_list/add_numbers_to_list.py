def add_numbers_to_list(nums: list):
    if len(nums) % 5 != 0:
        nums.append(nums[-1] + 1)
        add_numbers_to_list(nums)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    add_numbers_to_list(numbers)
    print(numbers)
