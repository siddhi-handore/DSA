def quick_sort(arr, low, high):
    i = low
    j = high
    pivot = arr[low]
    while i < j:
        while arr[i] <= pivot and i <= high:
            i += 1
        while arr[j] > pivot and j >= low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j


def quickSort(arr, low, high):
    if low < high:
        pindex = quick_sort(arr, low, high)
        quickSort(arr, low, pindex-1)
        quickSort(arr, pindex+1, high)


if __name__ == '__main__':
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    print(arr)
    n = len(arr)
    quickSort(arr, 0, n-1)
    print(arr)