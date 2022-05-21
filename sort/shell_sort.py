from sort import generate_data


def shell_sort(target: list[int]) -> list[int]:
    result = target.copy()
    data_count = len(result)
    swap_count = 0
    distance = len(target) // 4

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
    print(f'Target: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
