def firstOccur(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            ans = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans


def lastOccur(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            ans = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans


def countOccurrences(arr, x):
    # Write your code here.
    f = firstOccur(arr, x)
    if f == -1:
        return 0
    else:
        l = lastOccur(arr, x)
        return 1 + (l - f)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 4, 4, 5]
    print(countOccurrences(arr, 4))
