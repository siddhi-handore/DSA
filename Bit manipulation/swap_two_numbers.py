def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"Value of a {a}\nValue of b = {b}")
if __name__ == '__main__':
    a = 10
    b = 20
    print(f"Value of a {a}\nValue of b = {b}")
    swap(a, b)