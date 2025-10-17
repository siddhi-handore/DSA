def pattern(n):
    val = 1
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            if j == i or j == (2 * n - 2) - i:
                print(val, end="")
            else:
                print(" ", end="")
        print()
        if i < n - 1:
            val += 1
        else:
            val -= 1

if __name__ == '__main__':
    n = 5
    print(pattern(n))