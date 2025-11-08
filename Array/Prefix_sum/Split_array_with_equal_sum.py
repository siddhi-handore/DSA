def canSplit(arr):
    # code here
    n = len(arr)
    leftSum = 0
    rightSum = 0
    for i in arr:
        leftSum += i
    for i in range(n - 1, -1, -1):
        rightSum += arr[i]
        leftSum -= arr[i]

        if leftSum == rightSum:
            return i
            break
    return -1

def splitarr(arr):
    index = canSplit(arr)
    if index != -1:
        print(f"[{arr[0:index]}],[{arr[index:]}]")
    else:
        print(f"{[-1]}")

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 5]
    splitarr(arr)