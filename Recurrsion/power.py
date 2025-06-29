#Element n. Find n**p
def power(n, p):
    if p == 0:
        return 1
    return n * power(n, p-1)

n = int(input("Enter value of n->"))
p = int(input("Enter value of p->"))
print(power(n, p))