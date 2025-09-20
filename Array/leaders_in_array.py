def leaders(arr):
    st = []
    n = len(arr)
    st.append(arr[n-1])
    for i in range(n-2, -1, -1):
        if arr[i] > st[-1]:
            st.append(arr[i])
    st.reverse()
    return st

if __name__ == '__main__':
    arr = [10, 22, 12, 12, 3, 0, 6]
    print(leaders(arr))