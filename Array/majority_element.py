# Find the number that occurs more than N/2 time.
# Optimal solution using Moore's voting algorithm.
def majority(arr, n):
    element = arr[0]
    cnt = 0
    for i in range(n):
        if cnt == 0:
            element = arr[i]
        elif arr[i] == element:
            cnt+=1
        else:
            cnt-=1
    newcnt = 0
    for i in range(n):
        if arr[i] == element:
            newcnt+=1
    if newcnt > n//2:
        return element
    return -1

arr = [2, 3, 3, 3, 1, 2, 3]
n = len(arr)
print(majority(arr, n))