import array

symbols = ['d', 'f', 'h', 'e', 'a', 'g', 'k', 'n', 'c']
nums = [4, 104, 506, 78, 34, 22, 13, 39, 174, 82, 7]


def quick_sort(data: array) -> array:
    if len(data) < 2:
        return data

    pivot = data[len(data) // 2]
    less = [i for i in data if i < pivot]
    greater = [i for i in data if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    result = quick_sort(nums)
    print(result)


if __name__ == '__main__':
    main()
