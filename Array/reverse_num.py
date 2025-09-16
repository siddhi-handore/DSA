# def reverse_num(n):
#     rev = 0
#     while n!= 0:
#         num = n % 10
#         rev = rev * 10 + num
#         n = n//10
#     return rev

def reverse_num(n, rev):
    if n == 0:
        return 1
    rev *= 10 + n%10
    return reverse_num(n//10, rev)

n = 2435
rev = 0
print(reverse_num(n, rev))