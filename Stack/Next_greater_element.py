def nge(arr):
    result = [-1] * len(arr)
    st = []
    for i in range(len(arr)-1, -1, -1):
        while st and st[-1] < arr[i]:
            st.pop()
        if st and st[-1] > arr[i]:
            result[i] = st[-1]
        st.append(arr[i])
    return result

if __name__ == '__main__':
    arr = [5, 23, 9, 6, 12, 2, 0, 1]
    print(nge(arr))