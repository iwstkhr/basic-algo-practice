def gcd(x: int, y: int) -> int:
    return x if y == 0 else gcd(y, x % y)


def main() -> None:
    x, y = 8, 20
    result = gcd(x, y)
    print(result)


if __name__ == '__main__':
    main()
