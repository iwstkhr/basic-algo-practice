def search(target: str, keyword: str) -> int:
    """ Search for a keyword in a target string.

    Args:
        target (str): Target string
        keyword (str): Keyword to be searched for

    Returns:
        int: Index starting 0 if a keyword is found, otherwise -1
    """

    target_count = len(target)
    left = 0
    right = len(keyword)

    while right < target_count:
        distance = calc_move_distance(target[left:right], keyword)
        if distance == 0:
            return left

        left += distance
        right += distance

    return -1


def calc_move_distance(partial_target: str, keyword: str) -> int:
    """ Calculate move distance.

    Length of `partial_target` and `keyword` must be equal.

    Args:
        partial_target (str): Partial target string
        keyword (str): Keyword

    Returns:
        int: 0 if a partial target string is equal to a keyword, otherwise move distance
    """

    for i in range(len(partial_target) - 1, -1, -1):
        for j in range(i, -1, -1):
            if partial_target[i] != keyword[j]:
                continue

            if i == j:
                break
            else:
                return i - j
        else:
            return i + 1

    return 0


def main() -> None:
    target = 'HelloWorld'
    keyword = 'oWo'
    index = search(target, keyword)

    print(f'Found index: {index}')
    if index == -1:
        print('Result: Not found')
    else:
        print(f'Result: {target[index:index + len(keyword)]}')


if __name__ == '__main__':
    main()
