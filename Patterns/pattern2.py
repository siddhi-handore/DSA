def pattern(n):
    for i in range(n):
        for j in range(i):
            print("*", end="")
        print()
if __name__ == '__main__':
    n = 6
    pattern(n)
