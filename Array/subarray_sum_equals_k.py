def subarray(arr, k):
    preSum = 0
    cnt = 0
    prefixSum = {}
    for i in range(len(arr)):
        preSum += arr[i]
        if preSum - k in prefixSum:
            cnt += prefixSum[preSum - k]
        if preSum == k:
            cnt += 1
        if preSum in prefixSum:
            prefixSum[preSum] += 1
        else:
            prefixSum[preSum] = 1
    return cnt



if __name__ == '__main__':
    arr = [8, -1, -6, 6, 3, 0, 1, 2]
    print(subarray(arr, 3))