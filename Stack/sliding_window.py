from collections import deque
def maxOfSubarrays(arr, k):
    # code here
    res = []
    dq = deque()
    for i in range(0, k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    for i in range(k, len(arr)):
        res.append(arr[dq[0]])
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    res.append(arr[dq[0]])
    return res

if __name__ == '__main__':
    arr = [2, 10, 12, 1, 11]
    print(maxOfSubarrays(arr, 2))