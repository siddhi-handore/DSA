def prefixMax(arr):
    prefix = [0] * len(arr)
    for i in range(len(arr)):
        prefix[i] = max(prefix[i-1], arr[i])
    return prefix

if __name__ == '__main__':
    arr = [2, 1, 0, 5, 3]
    print(prefixMax(arr))