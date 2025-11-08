def count(n):
    cnt = 0
    while n > 0:
        n &= (n-1)
        cnt +=1
    return cnt

if __name__ == '__main__':
    n = 3
    print(count(n))