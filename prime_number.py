import math


def prime_numbers(to: int) -> list:
    primes = [2]

    for n in range(3, to + 1, 2):
        # Even numbers except 2 are always prime numbers,
        # so starting from 3 by stepping 2 can reduce calculation.

        for i in range(0, math.floor(math.sqrt(n))):
            if n % primes[i] == 0:
                # n is not a prime number.
                break
        else:
            # n is a prime number.
            primes.append(n)

    return primes


def main() -> None:
    to = 100
    primes = prime_numbers(to)
    print(primes)


if __name__ == '__main__':
    main()
