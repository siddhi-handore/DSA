def power(n):
    if n == 0:
        return False
    if n & (n-1) == 0:
        return True
    return False

if __name__ == '__main__':
    n = 3
    print(power(n))