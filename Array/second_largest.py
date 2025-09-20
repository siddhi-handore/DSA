def secondLargest(arr):
    largest = arr[0]
    slargest = -1

    for i in range(len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] > slargest and arr[i] != largest:
            slargest = arr[i]
    return slargest

if __name__ == '__main__':
    arr = [-1, -1, 28, 50, 35, 62, 77, 21, 100]
    print(secondLargest(arr))