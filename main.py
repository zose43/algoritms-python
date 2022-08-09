import array

input_data = [4, 5, 31, 64, 3312, 43, 90, 75, 84, 3, 29]


def find_smallest_element(data: array) -> int:
    smallest_element = data[0]
    index = 0
    for i in range(1, len(data)):
        if smallest_element > data[i]:
            smallest_element = data[i]
            index = i
    return index


def selection_sort(data: array) -> array:
    sort_array = []
    for i in range(len(data)):
        smallest_element = find_smallest_element(data)
        sort_array.append(data.pop(smallest_element))
    return sort_array


def main():
    result = selection_sort(input_data)
    print(result)


if __name__ == '__main__':
    main()
