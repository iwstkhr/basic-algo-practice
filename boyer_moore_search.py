def find(src: str, target: str) -> int:
    src_count = len(src)
    target_count = len(target)
    right_index = target_count - 1
    left_index = right_index - target_count + 1

    while right_index < src_count:
        move = 0
        match_count = 0

        for i in range(right_index, left_index - 1, -1):
            for j in range(target_count - match_count - 1, -1, -1):
                if src[i] == target[j]:
                    match_count += 1
                    break
                else:
                    move += 1

            if match_count == target_count:
                return left_index

            if move != 0:
                left_index += move
                right_index += move
                break

    return -1


def main() -> None:
    src = 'HelloWorld'
    target = 'oWo'
    index = find(src, target)
    print(f'Found index: {index}')
    if index == -1:
        print('Result: Not found')
    else:
        print(f'Result: {src[index:index + len(target)]}')


if __name__ == '__main__':
    main()
