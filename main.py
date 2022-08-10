def factorial(num: int) -> int:
    return 1 if num == 1 else num * factorial(num - 1)


def main():
    result = factorial(9)
    print(result)


if __name__ == '__main__':
    main()
