def select(arr, n):
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

if __name__ == '__main__':
    arr = [5, 8, 2, 3, 7, 1, 4]
    print(select(arr, len(arr)))