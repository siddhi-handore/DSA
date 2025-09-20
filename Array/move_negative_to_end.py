# Method 1: Bruteforce Solution
# TC: O(N) ,SC: O(N)
# def moveNeg(arr):
#     pos = []
#     neg = []
#     for i in arr:
#         if i < 0:
#             neg.append(i)
#         else:
#             pos.append(i)
#     for i in range(len(pos)):
#         arr[i] = pos[i]
#     n = len(pos)
#     for i in range(len(neg)):
#         arr[n] = neg[i]
#         n+=1
#     return arr

#Method 2: Better solution
# TC: O(n**2) SC:O(1)
def moveNeg(arr):
    n = len(arr)
    pos = 0

    for i in range(n):
        if arr[i] >= 0:
            temp = arr[i]
            k = i
            while k > pos:
                arr[k] = arr[k - 1]
                k -= 1
            arr[pos] = temp
            pos += 1
    return arr


if __name__ == '__main__':
    arr = [1, -1, 3, 2, -7, -5, 11, 6]
    print(moveNeg(arr))