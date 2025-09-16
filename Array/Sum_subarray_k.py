def subarraySum(arr, target):
    # Initialize window
    i, j = 0, 0
    res = []

    curr = 0
    for k in range(len(arr)):
        curr += arr[k]

        # If current sum becomes more or equal,
        # set end and try adjusting start
        if curr >= target:
            j = k

            # While current sum is greater,
            # remove starting elements of current window
            while curr > target and i < j:
                curr -= arr[i]
                i += 1

            # If we found a subarray
            if curr == target:
                res.append([i + 1, j + 1])
                return res

    # If no subarray is found
    return [-1]


if __name__ == "__main__":
    arr = [1,2,3,1]
    target = 4
    res = subarraySum(arr, target)

    print(" ".join(map(str, res)))