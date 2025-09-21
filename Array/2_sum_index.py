# Type 1 : Return indices of the two numbers
def twoSum(arr, k):
    n = len(arr)
    i = 0
    j = n-1
    res = []
    while i < j:
        tot = arr[i] + arr[j]
        if tot == k:
            res.append([i, j])
        if tot > k:
            j-=1
        else:
            i+=1
    return res

if __name__ == '__main__':
    arr = [2, 6, 5, 8, 11]
    print(twoSum(arr, 14))