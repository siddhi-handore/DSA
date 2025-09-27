# Brute force solution
def oneOccur(arr, n):
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i] == arr[j]:
                cnt += 1
        if cnt == 1:
            return arr[i]
    return -1

#Better Approach
def oneOccur(arr, n):
    freq = {}
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1
    for key, val in freq.items():
        if val == 1:
            return key
    return -1

# Optimal approach using XOR
def oneOccur(arr, n):
    XOR = 0
    for i in arr:
        XOR = XOR ^ i
    return XOR

if __name__ == '__main__':
    arr = [2, 5, 2, 7, 8, 1, 4, 4, 7, 8, 5]
    print(oneOccur(arr, len(arr)))