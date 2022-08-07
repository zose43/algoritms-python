import math
from typing import Union

nums = [4, 444, 34, 12, 45, 6, 19, 14, 72, 536, 2, 1, 777, 54, 66, 69]


def binary_search(data: list, guess: int) -> Union[int, str]:
    data.sort()
    high = len(data) - 1
    low = 0

    while low <= high:
        middle = math.floor((low + high) / 2)

        if guess == data[middle]:
            return guess
        if data[middle] > guess:
            high = middle - 1
        else:
            low = middle + 1

    return 'has no one'


def main() -> int:
    try:
        guess_key = input()
        if not guess_key.isdigit():
            raise Exception(f"Input value is not an integer: {guess_key}")

        print(binary_search(nums, int(guess_key)))
    except Exception as e:
        print(e)
    finally:
        return 0


if __name__ == '__main__':
    main()
