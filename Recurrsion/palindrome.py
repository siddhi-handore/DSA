def palindrome(name, n, i):
    if i > n/2:
        return True
    if name[n-1] != name[i]:
        return False
    return palindrome(name, n-1, i+1)

name = input("Enter a String->")
n = len(name)
print(palindrome(name, n, 0))