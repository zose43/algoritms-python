import array

data = [9, 4, 6]


def sums(nums: array) -> int:
    if len(nums) > 0:
        return nums.pop() + sums(nums)
    else:
        return 0


def main():
    result = sums(data)
    print(result)


if __name__ == '__main__':
    main()
