def print20(n):
    for i in range(0, n):
        for j in range(0, n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

n = 10
print20(n)