def selectionSort(sortOrder):
    data = [10, 5, 6, 23, 36, 43, 63, 12, 1, 2, 4]
    for i in range(len(data)):
        minIndex = i
        for j in range(i + 1, len(data)):
            if sortOrder(data[j], data[minIndex]):
                minIndex = j
        data[i], data[minIndex] = data[minIndex], data[i]
    print(data)


if __name__ == '__main__':
    selectionSort(lambda a, b: a < b)
    selectionSort(lambda a, b: a > b)
