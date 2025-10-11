def singleElement(arr, n):
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    low = 1
    high = n-2
    while low <= high:
        mid = (low+high)//2
        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]

        if (mid % 2 == 1 and arr[mid+1] == arr[mid]) or (mid % 2 == 0 and arr[mid+1] == arr[mid]):
            low = mid+1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    arr = [2, 2, 8, 7, 7, 15, 15, 20, 20]
    print(singleElement(arr, len(arr)))