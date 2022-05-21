import random


def generate_data(count: int) -> list:
    return [random.randint(1, count * 10) for _ in range(count)]


def create_frequency_distribution_table(src: list) -> list:
    table = [0] * (max(src) + 1)

    for i in range(len(src)):
        table[src[i]] += 1
    for i in range(1, len(table)):
        table[i] += table[i - 1]

    return table


def counting_sort(src: list, table: list) -> list:
    result = [None] * len(src)

    for i in range(len(src) - 1, -1, -1):
        pos = table[src[i]]
        result[pos - 1] = src[i]
        table[src[i]] -= 1

    return result


def main() -> None:
    count = 1000
    data = generate_data(count)
    table = create_frequency_distribution_table(data)
    result = counting_sort(data, table)
    print(f'Source: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
