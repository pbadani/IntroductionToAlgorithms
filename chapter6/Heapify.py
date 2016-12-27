def leftChildIndex(i):
    return i * 2 + 1


def rightChildIndex(i):
    return leftChildIndex(i) + 1


def getChildIndex(i):
    return leftChildIndex(i), rightChildIndex(i)


def recursiveHeapify(arr, i, heapOrder):
    other = heapOrder(arr, i)
    if other != i:
        arr[i], arr[other] = arr[other], arr[i]
        recursiveHeapify(arr, other, heapOrder)


def iterativeHeapify(arr, i, heapOrder):
    while i < len(arr):
        other = heapOrder(arr, i)
        if other != i:
            arr[i], arr[other] = arr[other], arr[i]
            i = other
        else:
            break


def maxHeap(arr, i):
    left, right = getChildIndex(i)
    largest = i
    if left < len(arr) and arr[left] > arr[i]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    return largest


def minHeap(arr, i):
    left, right = getChildIndex(i)
    smallest = i
    if left < len(arr) and arr[left] < arr[i]:
        smallest = left
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    return smallest


if __name__ == '__main__':
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(arr)
    recursiveHeapify(arr, 1, maxHeap)
    print(arr)

    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(arr)
    iterativeHeapify(arr, 1, maxHeap)
    print(arr)

    arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    print(arr)
    recursiveHeapify(arr, 2, maxHeap)
    print(arr)

    arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    print(arr)
    iterativeHeapify(arr, 2, maxHeap)
    print(arr)
