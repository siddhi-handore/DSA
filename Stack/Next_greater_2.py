def nge2(arr):
    n = len(arr)
    nge = [0] * n
    st = []
    for i in range(2*(n-1), -1, -1):
        while st and st[-1] <= arr[i%n]:
            st.pop()
        if i < n:
            nge[i] = -1 if not st else st[-1]
        st.append(arr[i%n])
    return nge

if __name__ == '__main__':
    arr = [2, 10, 12, 1, 11]
    print(nge2(arr))