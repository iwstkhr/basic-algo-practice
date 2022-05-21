import random


def generate_data(count: int) -> list:
    return [random.randint(1, count * 10) for _ in range(count)]


def shell_sort(src: list) -> list:
    result = src.copy()
    data_count = len(result)
    swap_count = 0
    distance = len(src) // 4

    while distance > 0:
        for i in range(distance, data_count, distance):
            for j in range(i - distance, 0, -distance):
                if result[j] < result[j - distance]:
                    result[j - distance], result[j] = result[j], result[j - distance]
                    swap_count += 1

        distance //= 4

    print(f'Swap count: {swap_count}')
    return result


def main() -> None:
    count = 1000
    data = generate_data(count)
    result = shell_sort(data)
    print(f'Source: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
