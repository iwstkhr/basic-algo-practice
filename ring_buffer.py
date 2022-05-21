class RingBuffer:
    __buffer = None
    __size = 0
    __start = 0
    __end = 0
    __count = 0

    def __init__(self, size: int):
        self.__buffer = [None] * size
        self.__size = size

    def __len__(self):
        return self.__count

    def is_empty(self) -> bool:
        return self.__count < self.__size

    def enqueue(self, value: any) -> list:
        if not self.is_empty():
            raise ValueError

        self.__buffer[self.__end] = value
        self.__count += 1

        self.__end += 1
        if self.__size == self.__end:
            self.__end = 0

        return self.__buffer

    def dequeue(self) -> any:
        if self.__count == 0:
            return None

        data = self.__buffer[self.__start]
        self.__count -= 1

        self.__start += 1
        if self.__size == self.__start:
            self.__start = 0

        return data

    def clear(self) -> None:
        self.__buffer = [None] * self.__size
        self.__start = 0
        self.__end = 0
        self.__count = 0

    def peek(self) -> any:
        return self.__buffer[self.__start]

    def __str__(self):
        result = ''

        if self.__start < self.__end:
            for i in range(self.__start, self.__end):
                result += f'{self.__buffer[i]}, '
            return result[:-2]

        else:
            for i in range(self.__start, self.__size):
                result += f'{self.__buffer[i]}, '
            for i in range(0, self.__end):
                result += f'{self.__buffer[i]}, '

            return result[:-2]


def main() -> None:
    size = 3
    ring_buffer = RingBuffer(size)

    ring_buffer.enqueue(1)
    ring_buffer.enqueue(2)
    print(ring_buffer)  # 1, 2

    print(ring_buffer.dequeue())  # 1
    print(ring_buffer)  # 2

    ring_buffer.enqueue(3)
    ring_buffer.enqueue(4)
    print(ring_buffer)  # 2, 3, 4

    print(ring_buffer.dequeue())  # 2
    print(ring_buffer)  # 3, 4

    print(ring_buffer.dequeue())  # 3
    print(ring_buffer.dequeue())  # 4
    print(ring_buffer.dequeue())  # None


if __name__ == '__main__':
    main()
