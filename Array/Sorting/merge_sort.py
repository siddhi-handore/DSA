def merge(arr, low, mid, high):
    left = low
    right = mid+1
    ans = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            ans.append(arr[left])
            left+=1
        else:
            ans.append(arr[right])
            right+=1
    while left <= mid:
        ans.append(arr[left])
        left+=1
    while right <= high:
        ans.append(arr[right])
        right+=1
    for i in range(len(ans)):
        arr[low + i] = ans[i]

def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)



if __name__ == '__main__':
    arr = [3, 2, 4, 1, 3]
    mergeSort(arr, 0, len(arr)-1)
    print(arr)