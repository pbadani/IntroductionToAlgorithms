def binarySearch(data, n):
    l = 0
    r = len(data) - 1
    while r - l > 1:
        mid = (l + r) // 2
        if data[mid] == n:
            return mid
        elif data[mid] < n:
            l = mid + 1
        else:
            r = mid - 1

    return None


if __name__ == '__main__':
    data = [1, 2, 4, 5, 6, 10, 12, 23, 43, 63, 66]
    print(binarySearch(data, 43))
