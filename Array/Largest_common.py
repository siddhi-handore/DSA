def LargestCommon(arr1, arr2):
    st = set(arr1)
    maxi = -1
    for i in arr2:
        if i in st:
            maxi = max(i, maxi)
    return maxi

if __name__ == '__main__':
    arr1 = [3, 1, 5, 2, 6]
    arr2 = [1, 8, 12, 2, 5]
    print(LargestCommon(arr1, arr2))
