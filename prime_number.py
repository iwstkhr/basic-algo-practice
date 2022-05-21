import math


def find_prime_numbers(to: int) -> list[int]:
    """ Find prime numbers.

    Args:
        to (int): Max number

    Returns:
        list[int]: Prime numbers up to a max number
    """

    primes = [2]  # Two is a prime number.

    for n in range(3, to + 1, 2):
        # Starting from 3 by stepping 2 can reduce calculation
        # because no even numbers except 2 are prime numbers.

        if is_prime_number(n, primes):
            primes.append(n)

    return primes


def is_prime_number(target: int, primes: list[int]) -> bool:
    """ Check whether a target value is a prime number.

    Args:
        target (int): Target value to be checked
        primes (list[int]): Prime numbers already found

    Returns:
        bool: True if a target value is a prime number
    """

    for i in range(0, math.floor(math.sqrt(target))):
        if target % primes[i] == 0:
            # Not a prime number.
            return False

    return True


def main() -> None:
    to = 100
    primes = find_prime_numbers(to)
    print(primes)


if __name__ == '__main__':
    main()
