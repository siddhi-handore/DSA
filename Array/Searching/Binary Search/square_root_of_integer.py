def square(n):
    low = 1
    high = n
    ans = 1
    while low <= high:
        mid = (low+high)//2
        if (mid * mid) <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return high

if __name__ == '__main__':
    n = 24
    print(square(8))