def upperBound(arr, x):
    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

if __name__ == '__main__':
    arr = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]
    print(upperBound(arr, 13))