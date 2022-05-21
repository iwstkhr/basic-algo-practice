from sort import generate_data


def bubble_sort(target: list[int]) -> list[int]:
    """ Bubble sort function

    Args:
        target (list[int]): List to be sorted

    Returns:
        list[int]: Sorted list
    """

    result = target.copy()
    total_swap_count = 0
    right_index = len(result) - 1

    while 0 < right_index:
        swap_count = 0

        for i in range(right_index, 0, -1):
            # Scan elements from right to left.

            if result[i] < result[i - 1]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swap_count += 1
                total_swap_count += 1

        if swap_count == 0:
            # If swap had not occurred in this path, sorting has already completed.
            break

    print(f'Total swap count: {total_swap_count}')
    return result


def main() -> None:
    count = 1000
    data = generate_data(count)
    result = bubble_sort(data)
    print(f'Target: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
