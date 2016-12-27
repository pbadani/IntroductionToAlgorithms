def merge(data, p, q, r):
    a = []
    b = []
    for i in range(p, q + 1):
        a.append(data[i])
    a.append(1024)
    for i in range(q + 1, r + 1):
        b.append(data[i])
    b.append(1024)

    m = 0
    n = 0
    for i in range(p, r + 1):
        if b[n] == 1024 or a[m] < b[n]:
            data[i] = a[m]
            m += 1
        else:
            data[i] = b[n]
            n += 1


def mergeSort(data, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(data, p, q)
        mergeSort(data, q + 1, r)
        merge(data, p, q, r)


def mergeSortMain():
    data = [10, 5, 6, 23, 36, 43, 63, 12, 1, 2, 4]
    mergeSort(data, 0, 10)
    print(data)


if __name__ == '__main__':
    mergeSortMain()
