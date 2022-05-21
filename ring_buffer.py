class RingBufferFullError(Exception):
    pass


class RingBuffer:
    def __init__(self, size: int):
        self.__buffer = [None] * size
        self.__size = size
        self.__start = 0
        self.__end = 0
        self.__count = 0

    def __len__(self):
        return self.__count

    def is_full(self) -> bool:
        """ Check whether the ring buffer is full.

        Returns:
            bool: True if it is full
        """

        return self.__count == self.__size

    def is_empty(self) -> bool:
        """ Check whether the ring buffer is empty.

        Returns:
            bool: True if it is empty
        """

        return self.__count == 0

    def enqueue(self, value: any) -> list:
        """ Queue a value.

        Args:
            value: Value to be queued

        Returns:
            list: Ring buffer contains a new value
        """

        if self.is_full():
            raise RingBufferFullError

        # Enqueue the value to the last element,
        # then increment the counter and the end pointer.
        # e.g.
        # 9,8, , ,7,6
        #     E     S
        # Queue "5"
        # 9,8,5, ,7,6
        #       E   S
        self.__buffer[self.__end] = value
        self.__count += 1
        self.__end += 1

        if self.__size == self.__end:
            # Reset the end pointer if it reached at the buffer size.
            self.__end = 0

        return self.__buffer

    def dequeue(self) -> any:
        """ Dequeue the first value. (FIFO)

        Returns:
            any: First value
        """

        if self.is_empty():
            return None

        # Dequeue the value from the last element,
        # then decrement the counter and increment the start pointer.
        # e.g.
        # 9,8, , ,7,6
        #     E     S
        # Dequeue
        # 9,8,5, ,7,
        # S     E
        data = self.__buffer[self.__start]
        self.__buffer[self.__start] = None
        self.__count -= 1
        self.__start += 1

        if self.__size == self.__start:
            self.__start = 0

        return data

    def clear(self) -> None:
        """ Clear the ring buffer. """

        self.__buffer = [None] * self.__size
        self.__start = 0
        self.__end = 0
        self.__count = 0

    def peek(self) -> any:
        """ Check the first value without dequeue. """

        return self.__buffer[self.__start]

    def __str__(self):
        if self.__start < self.__end:
            return ', '.join([str(self.__buffer[i]) for i in range(self.__start, self.__end)])
        else:
            result = ', '.join([str(self.__buffer[i]) for i in range(self.__start, self.__size)])
            result += ', ' + ', '.join([str(self.__buffer[i]) for i in range(0, self.__end)])
            return result


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
    print(ring_buffer.is_full())  # True

    print(ring_buffer.dequeue())  # 2
    print(ring_buffer)  # 3, 4

    print(ring_buffer.dequeue())  # 3
    print(ring_buffer.dequeue())  # 4
    print(ring_buffer.dequeue())  # None


if __name__ == '__main__':
    main()
