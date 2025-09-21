def threeSum(arr, t):
    n = len(arr)
    res = []
    arr.sort()
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i+1
        k = n-1
        while j < k:
            tot = arr[i] + arr[j] + arr[k]

            if tot < t:
                j+=1
            elif tot > t:
                k-=1
            else:
                res.append([arr[i], arr[j], arr[k]])
                j+=1
                k-=1
                while arr[j] == arr[j-1] and j < k:
                    j+=1
                while arr[k] == arr[k + 1] and k > j:
                    k -= 1
    return res

if __name__ == '__main__':
    arr = [-1, 0, 1, 2, -1, -4]
    print(threeSum(arr, 0))