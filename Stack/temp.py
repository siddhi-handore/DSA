def nextGreater(arr, n):
    st = []
    res = [-1] * n
    for i in range(2*(n-1), -1, -1):
        while st and st[-1] < arr[i%n]:
            st.pop()
        if st and i < n:
            res[i%n] = st[-1]
        else:
            res[i%n] = -1
        st.append(arr[i%n])
    return res

if __name__ == '__main__':
    arr = [8, 12, 5, 15, 25, 3, 0, 1, 30]
    print(nextGreater(arr, len(arr)))
