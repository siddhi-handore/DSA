def Bs(mat, m):
    low = 0
    high = m
    ans = m
    while low <= high:
        mid = (low + high)//2
        if mat[mid] == 1:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
def maxOnes(mat):
    n = len(mat)
    m = len(mat[0])
    maxcnt = -1
    index = -1
    for i in range(n):
        cnt = m - Bs(mat[i], m-1)
        if cnt > maxcnt:
            index = i
            maxcnt = cnt
    return index

if __name__ == '__main__':
    mat = [[0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1]]
    print(maxOnes(mat))