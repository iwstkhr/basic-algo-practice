import random


def generate_data(count: int) -> list[int]:
    """ Generate a list containing randomized integer numbers.

    Args:
        count (int): Data count

    Returns:
        list[int]: List containing randomized integer numbers
    """

    return [random.randint(1, count * 10) for _ in range(count)]
