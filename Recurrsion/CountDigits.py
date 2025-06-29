#Functional way of recurssion
def CountDigits(n):
    if n == 0:
        return 0
    return CountDigits(n//10) + (n%10)

n = int(input("Enter a number->"))
print(CountDigits(n))