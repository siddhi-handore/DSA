# Brute force approach
def turnoff(n):
    if n == 0:
        return 0
    pos = 0
    while((n >> pos) & 1 == 0):
        pos += 1

    n = n ^ (1<<pos)
    return n

# Expected approach
def turnOff(n):
    if n == 0:
        return 0
    return (n & (n-1))

# Using 2's compliment
def Trunoff(n):
    if n == 0:
        return 0
    n -= (n & (not n))
    return n
if __name__ == '__main__':
    n = 5
    print(turnOff(n))