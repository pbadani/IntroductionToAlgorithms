def insertionSort(sortOrder):
    data = [10, 5, 6, 23, 6, 43, 63, 12, 1, 2, 4]

    for index in range(1, len(data)):
        current = data[index]
        while index > 0 and sortOrder(current, data[index - 1]):
            data[index] = data[index - 1]
            index -= 1
        data[index] = current

    print(data)


if __name__ == "__main__":
    ascending = lambda a, b: a < b
    insertionSort(ascending)

    descending = lambda a, b: a > b
    insertionSort(descending)
