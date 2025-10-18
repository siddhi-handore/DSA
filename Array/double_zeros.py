def dup(arr, n):
    zeros = arr.count(0)
    i = n-1
    j = n + zeros - 1
    while i < j:
        if j < n:
            arr[j] = arr[i]
        if arr[i] == 0:
            j-=1
            if j<n:
                arr[j] = 0
        i-=1
        j-=1

if __name__ == '__main__':
    arr = [1, 0, 2, 0]
    print(arr)
    dup(arr, len(arr))
    print(arr)