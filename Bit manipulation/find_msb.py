def msb(n):
    if n == 0:
        return 0
    msb = 0
    n = n //2
    while n > 0:
        n = n // 2
        msb += 1
    return (1<<msb)

if __name__ == '__main__':
    n = 10
    print(msb(12))