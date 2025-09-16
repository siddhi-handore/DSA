def print18(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print("*", end=" ")
        for j in range(0, 2*i):
            print(" ", end=" ")
        for j in range(0, n-i):
            print("*", end=" ")
        print()
    for i in range(1, n+1):
        for j in range(0, i):
            print("*", end=" ")
        for j in range(0, 2*(n-i)):
            print(" ", end=" ")
        for j in range(0, i):
            print("*", end=" ")
        print()
n = 5
print18(n)
