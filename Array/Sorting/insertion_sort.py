def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    arr = [12, 5, 10, 25, 47, 99, 50]
    print(insertionSort(arr))

