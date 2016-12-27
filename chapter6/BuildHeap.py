from chapter6.Heapify import recursiveHeapify, maxHeap, minHeap, iterativeHeapify


def buildHeapRecursively(arr, heapOrder):
    for i in range(len(arr) // 2, -1, -1):
        recursiveHeapify(arr, i, heapOrder)


def buildHeapIteratively(arr, heapOrder):
    for i in range(len(arr) // 2, -1, -1):
        iterativeHeapify(arr, i, heapOrder)

if __name__ == '__main__':
    arr = [2, 16, 4, 10, 14, 17, 9, 13, 23, 28, 1]
    print(arr)
    buildHeapRecursively(arr, maxHeap)
    print(arr)

    arr = [2, 16, 4, 10, 14, 17, 9, 13, 23, 28, 1]
    print(arr)
    buildHeapIteratively(arr, maxHeap)
    print(arr)

    arr = [2, 16, 4, 10, 14, 17, 9, 13, 23, 28, 1]
    print(arr)
    buildHeapRecursively(arr, minHeap)
    print(arr)

    arr = [2, 16, 4, 10, 14, 17, 9, 13, 23, 28, 1]
    print(arr)
    buildHeapIteratively(arr, minHeap)
    print(arr)
