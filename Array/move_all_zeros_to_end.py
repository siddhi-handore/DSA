#move all zeros to the end
def move_to_end(arr):
    n = len(arr)
    ind = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[ind] = arr[ind], arr[i]
            ind+= 1
    return arr




if __name__ == '__main__':
    arr = [0, 4, 0, 5, 8, 0, 16]
    print(move_to_end(arr))