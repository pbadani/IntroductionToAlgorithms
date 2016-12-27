from chapter6.BuildHeap import buildHeapRecursively
from chapter6.Heapify import recursiveHeapify, maxHeap, minHeap


def heapSort(arr, heapify, heapOrder):
    sol = []
    buildHeapRecursively(arr, heapOrder)
    for i in range(len(arr) - 1, -1, -1):
        sol.append(arr[0])
        arr[0] = arr[i]
        del arr[i]
        heapify(arr, 0, heapOrder)

    return sol


if __name__ == '__main__':
    arr = [2, 16, 4, 10, 14, 17, 9, 13, 23, 28, 1]
    print(arr)
    sol = heapSort(arr, recursiveHeapify, maxHeap)
    print(sol)

    arr = [2, 16, 4, 10, 14, 17, 9, 13, 23, 28, 1]
    print(arr)
    sol = heapSort(arr, recursiveHeapify, minHeap)
    print(sol)

    arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print(arr)
    sol = heapSort(arr, recursiveHeapify, maxHeap)
    print(sol)

    arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print(arr)
    sol = heapSort(arr, recursiveHeapify, minHeap)
    print(sol)