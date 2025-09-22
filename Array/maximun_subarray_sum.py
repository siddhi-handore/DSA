# Kadane's algorithm
def kadane(arr):
    tot = 0
    maxi = float('-inf')
    ansStart = -1
    ansEnd = -1
    start = 0
    for i in range(len(arr)):
        tot += arr[i]

        if tot > maxi:
            maxi = tot
            ansStart = start
            ansEnd = i

        if tot < 0:
            tot = 0
            start = i+1
    return [ansStart, ansEnd]

if __name__ == '__main__':
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(kadane(arr))