# def missing(arr, n):
#     for num in range(1, n+1):
#         found = False
#         for x in arr:
#             if x == num:
#                 found = True
#                 break
#         if not found:
#             return num

# Optimal solution
# TC: O(N) SC:O(1)
def missing(arr, n):
    XOR1 = 0
    XOR2 = 0
    for i in range(n-1):
        XOR2 = XOR2 ^ arr[i]
        XOR1 = XOR1 ^ (i+1)
    return XOR1 ^ XOR2

# Optimal solution
# TC: O(N)  SC:O(1)
# def missing(arr, n):
#     num = n*(n+1)//2
#     tot = sum(arr)
#     return num - tot

if __name__ == '__main__':
    arr = [0, 1, 2, 4]
    n = len(arr)
    print(missing(arr, n))