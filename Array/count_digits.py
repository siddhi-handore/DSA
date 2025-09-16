def count_digits(n):
    if n < 10:
        return 1
    cnt = 0
    while n != 0:
        num = n % 10
        cnt += 1
        n = n//10
    return cnt



# Recursive method

# def count_n(n):
#     if n < 10:
#         return 1
#     return 1 + count_n(n//10)

n = 1223890
print(count_digits(n))