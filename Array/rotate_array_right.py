def reverse(start, end, arr):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotate(arr, d):
    n = len(arr)
    if d == 0:
        return arr
    d = d % n
    reverse(0, n-d-1, arr)
    reverse(n-d, n-1, arr)
    reverse(0, n-1, arr)
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(rotate(arr, 2))

