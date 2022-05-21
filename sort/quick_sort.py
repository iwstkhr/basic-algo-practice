from sort import generate_data


def quick_sort(target: list[int], left: int, right: int) -> list[int]:
    """ Quick sort function

    Args:
        target (list[int]): List to be sorted
        left (int): Left index
        right (int): Right index

    Returns:
        list[int]: Sorted list
    """

    result = target.copy()
    # Make a partition based on a pivot.
    result, partition_left, partition_right = partition(result, left, right)

    if left < partition_right:
        result = quick_sort(result, left, partition_right)
    if partition_left < right:
        result = quick_sort(result, partition_left, right)

    return result


def partition(target: list[int], left: int, right: int) -> (list[int], int, int):
    """ Make a partition based on a pivot.

    Args:
        target (list[int]): List to be partitioned
        left (int): Left index
        right (int): Right index

    Returns:
        tuple (list[int], int, int): Partitioned list, Left index of a partition, Right index of a partition
    """

    result = target.copy()
    pivot = get_pivot(target, left, right)

    while left <= right:
        while result[left] < pivot:
            left += 1
        while result[right] > pivot:
            right -= 1

        if left <= right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

    return result, left, right


def get_pivot(target: list[int], left: int, right: int) -> int:
    """ Get a pivot using a center index of a target list.

    Args:
        target (list[int]): Target list
        left (int): Left index
        right (int): Right index

    Returns:
        int: Pivot
    """

    center = (left + right) // 2
    return target[center]


def main() -> None:
    count = 1000
    data = generate_data(count)
    result = quick_sort(data, 0, len(data) - 1)
    print(f'Target: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
