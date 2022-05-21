import random


def generate_data(count: int) -> list:
    return [random.randint(1, count * 10) for _ in range(count)]


def quick_sort(src: list, left: int, right: int):
    result = src.copy()
    left_index = left
    right_index = right
    center = (left + right) // 2
    pivot = result[center]

    while left_index <= right_index:
        while result[left_index] < pivot:
            left_index += 1
        while result[right_index] > pivot:
            right_index -= 1

        if left_index <= right_index:
            result[left_index], result[right_index] = result[right_index], result[left_index]
            left_index += 1
            right_index -= 1

    if left < right_index:
        result = quick_sort(result, left, right_index)
    if left_index < right:
        result = quick_sort(result, left_index, right)

    return result


def main() -> None:
    count = 1000
    data = generate_data(count)
    result = quick_sort(data, 0, len(data) - 1)
    print(f'Source: {data}')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
