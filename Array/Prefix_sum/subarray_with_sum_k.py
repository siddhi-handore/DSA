def sub(arr, k):
    preSum = 0
    n = len(arr)
    mp = {}
    cnt = 0
    for i in range(n):
        preSum += arr[i]
        if preSum == k:
            cnt += 1
        elif preSum - k in mp:
            cnt += mp[preSum-k]
        if preSum not in mp:
            mp[preSum] = 1
    return cnt

if __name__ == '__main__':
    arr = [9, 4, 0, 20, 3, 10, 5]
    print(sub(arr, 0))