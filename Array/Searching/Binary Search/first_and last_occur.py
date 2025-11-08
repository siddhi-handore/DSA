def firstOccr(arr, n, k):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low + high )//2
        if arr[mid] == k:
            ans = mid
            high = mid - 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return ans
def lastOccr(arr, n, k):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low + high )//2
        if arr[mid] == k:
            ans = mid
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return ans
def firstAndLastPosition(arr, n, k):
    f = firstOccr(arr, n, k)
    if f == -1:
        return [-1, -1]
    l = lastOccr(arr, n, k)
    return [f, l]

if __name__ == '__main__':
    arr = [0, 0, 1, 1, 2, 2, 2, 2]
    k = 2
    print(firstAndLastPosition(arr, len(arr), k))