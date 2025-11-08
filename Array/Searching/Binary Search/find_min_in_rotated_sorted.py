def findMin(nums, n):
    low = 0
    high = len(nums) - 1
    ans = float('inf')
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[mid]:
            ans = min(ans, nums[low])
            low = mid + 1
        else:
            ans = min(ans, nums[mid])
            high = mid - 1
    return ans

if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(findMin(arr, len(arr)))