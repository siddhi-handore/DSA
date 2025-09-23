# Write recursive binary search


def binary(arr, t):
    n = len(arr)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == t:
            return True
        elif arr[mid] < t:
            low = mid+1
        else:
            high = mid-1

    return False

if __name__ == '__main__':
    arr = [1, 3, 25, 50, 68, 99, 105]
    t = 105
    print(binary(arr, t))
