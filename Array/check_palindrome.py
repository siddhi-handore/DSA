# # Check Palindrome string
def check_palindrome(s):
    n = len(s)
    j = n-1
    i = 0
    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

s = "siddhi"
print(check_palindrome(s))

# Check Palindrome number

def reverse_num(num):
    rev = 0
    while num!=0:
        n = num%10
        rev = rev * 10 + n
        num = num // 10
    return rev
def palindrome_num(num):
    if num == reverse_num(num):
        return True
    return False

num = 12345
print(palindrome_num(num))