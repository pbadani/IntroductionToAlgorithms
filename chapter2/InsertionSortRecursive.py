def insertionSort(data, n):
    if n == 0:
        return
    else:
        insertionSort(data, n - 1)
        index = n - 1
        current = data[n]
        while current < data[index] and index > -1:
            data[index + 1] = data[index]
            index -= 1
        data[index + 1] = current


def insertionSortRecursive():
    data = [10, 5, 6, 23, 36, 43, 63, 12, 1, 2, 4]
    insertionSort(data, len(data) - 1)
    print(data)


if __name__ == '__main__':
    insertionSortRecursive()
