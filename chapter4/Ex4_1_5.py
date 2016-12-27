def findMaxSubArray(arr):
    left = right = 0
    max = arr[0]
    for i in range(1, len(arr)):
        ileft = i
        iright = i
        sum = imax = arr[i]
        for j in range(i - 1, -1, -1):
            sum += arr[j]
            if sum > imax:
                imax = sum
                ileft = j

        if imax > max:
            left = ileft
            right = iright
            max = imax

    print("%s %s %s" % (left, right, max))


if __name__ == '__main__':
    data = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    # data = [-1, 2, 3, 5, -2]
    arr = [data[i] - data[i - 1] for i in range(1, len(data))]
    findMaxSubArray(arr)
