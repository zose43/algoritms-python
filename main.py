import array

numbers = [200, 23, 12, 21, 104, 44, 54, 65, 5, 3, 98, 27]


def find_bg(data: array) -> int:
    if len(data) == 2:
        return data[0] if data[0] > data[1] else data[1]

    sub_max = find_bg(data[1:])
    return sub_max if data[0] < sub_max else data[0]


def main():
    print(find_bg(numbers))


if __name__ == '__main__':
    main()
