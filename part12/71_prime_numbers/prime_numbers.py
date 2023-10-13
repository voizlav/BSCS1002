def prime_numbers():
    prime = 2
    while True:
        is_prime = True
        for i in range(2, prime):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            yield prime
        prime += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
