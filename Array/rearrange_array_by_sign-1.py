#Brute force solution
def rearrange(arr, n):
    pos = []
    neg = []
    for i in arr:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    for i in range(n//2):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]
    return arr

#Optimal solution
def rearrange(arr, n):
    pos = 0
    neg = 1
    ans = [0] * n
    for i in range(n):
        if arr[i] >= 0:
            ans[pos] = arr[i]
            pos += 2
        else:
            ans[neg] = arr[i]
            neg += 2
    return ans

if __name__ == '__main__':
    arr = [3, 1, -2, -5, 2, -4]
    print(rearrange(arr, len(arr)))
