def search(arr, t):
    for i in arr:
        if i == t:
            return True
    return False

if __name__ == '__main__':
    arr = [1, 90, 45, 75, 46, 29, 633, 23]
    t = 90
    print(search(arr, t))