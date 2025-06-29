def NToOne(n):
    if n == 0:
        return
    print(n, end=" ")
    NToOne(n-1)

n = int(input("Enter a number->"))
NToOne(n)