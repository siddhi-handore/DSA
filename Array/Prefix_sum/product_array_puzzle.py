def productExceptSelf(arr):
    # code here
    n = len(arr)
    res = [0] * n
    zerocnt = 0
    preSum = 1
    for i in arr:
        if i == 0:
            zerocnt += 1
        else:
            preSum *= i
    if zerocnt > 1:
        return res
    elif zerocnt == 1:
        for i in range(n):
            if arr[i] == 0:
                res[i] = preSum
        return res
    else:
        print(preSum)
        for i in range(n):
            res[i] = preSum // arr[i]
        return res

if __name__ == '__main__':
    arr = [1, 2, 0, 4]
    print(productExceptSelf(arr))
