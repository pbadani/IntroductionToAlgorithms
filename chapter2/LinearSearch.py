def linearSearch(value):
    data = [10, 5, 6, 23, 6, 43, 63, 12, 1, 2, 4]
    for index in range(len(data)):
        if (data[index] == value):
            return index
    return None


if __name__ == '__main__':
    print(linearSearch(23))
    print(linearSearch(24))
