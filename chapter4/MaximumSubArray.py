def findMaxCrossingSubArray(arr, low, mid, high):
    maxLeftSum = 0
    leftSum = 0
    left = mid - 1
    for i in range(mid, low - 1, -1):
        leftSum += arr[i]
        if leftSum > maxLeftSum:
            maxLeftSum = leftSum
            left = i

    maxRightSum = 0
    rightSum = 0
    right = mid
    for i in range(mid + 1, high + 1, 1):
        rightSum += arr[i]
        if rightSum > maxRightSum:
            maxRightSum = rightSum
            right = i

    return left, right, maxLeftSum + maxRightSum


def findMaxSubArray(arr, low, high):
    if low == high:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        leftLow, leftHigh, leftSum = findMaxSubArray(arr, low, mid)
        rightLow, rightHigh, rightSum = findMaxSubArray(arr, mid + 1, high)
        crossLow, crossHigh, crossSum = findMaxCrossingSubArray(arr, low, mid, high)
        if leftSum > rightSum and leftSum > crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum > leftSum and rightSum > crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum


if __name__ == '__main__':
    data = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    # data = [-2, -3, 4, -1, -2, 1, 5, 3]
    # data = [-1, 2, 3, 5, -2]
    arr = [data[i] - data[i - 1] for i in range(1, len(data))]
    low, high, sum = findMaxSubArray(arr, 0, len(arr) - 1)
    print('Low:%s, High:%s, Sum:%s' % (low, high, sum))
