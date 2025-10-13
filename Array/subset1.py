def subset(arr, ans, i):
    if i == len(arr):
        print(ans)
        return
    ans.append(arr[i])
    subset(arr, ans, i+1)
    ans.remove(arr[i])
    subset(arr, ans, i+1)

if __name__ == '__main__':
    arr = [1, 2, 3]
    subset(arr, [], 0)