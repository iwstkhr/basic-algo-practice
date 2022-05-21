import random


def generate_data(count: int) -> list:
    return [random.randint(1, count * 10) for _ in range(count)]


def bubble_sort(src: list) -> list:
    result = src.copy()
    swap_count = 0
    right_index = len(result) - 1
    left_index = 0

    while left_index < right_index:
        path_swap_count = 0

        for i in range(right_index, left_index, -1):
            # Scan elements from right to left.

            if result[i] < result[i - 1]:
                result[i - 1], result[i] = result[i], result[i - 1]
                path_swap_count += 1
                swap_count += 1
                to_index = i

        if path_swap_count == 0:
            # If swap had not occurred in this path, sorting has already completed.
            break

    print(f'Swap count: {swap_count}')
    return result


def main() -> None:
    count = 1000
    data = generate_data(count)
    result = bubble_sort(data)
    print(f'Source: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
