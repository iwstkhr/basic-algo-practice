from sort import generate_data


def create_frequency_distribution_table(target: list[int]) -> list[int]:
    """ Create a frequency distribution table.
    e.g.)
    target = [0, 5, 2, 8, 3, 5]
    table = [1, 0, 1, 1, 0, 2, 0, 0, 1]
            -> [1, 1, 2, 3, 3, 5, 5, 5, 6]

    Args:
        target (list[int]): List to be sorted

    Returns:
        list[int]: Frequency distribution table
    """

    table = [0] * (max(target) + 1)

    for i in range(len(target)):
        table[target[i]] += 1
    for i in range(1, len(table)):
        table[i] += table[i - 1]

    return table


def counting_sort(target: list[int], table: list[int]) -> list[int]:
    """ Counting sort function

    Args:
        target (list[int]): List to be sorted
        table (list[int]): Frequency distribution table

    Returns:
        list[int]: Sorted list
    """

    result = [None] * len(target)

    for i in range(len(target) - 1, -1, -1):
        pos = table[target[i]]
        result[pos - 1] = target[i]
        table[target[i]] -= 1

    return result


def main() -> None:
    count = 10
    data = generate_data(count)
    table = create_frequency_distribution_table(data)
    result = counting_sort(data, table)
    print(f'Target: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
