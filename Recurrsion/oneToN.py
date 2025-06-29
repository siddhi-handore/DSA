def oneToN(n):
    if n == 0:
        return
    oneToN(n-1)
    print(n, end=" ")

n = int(input("Enter a number->"))
oneToN(n)