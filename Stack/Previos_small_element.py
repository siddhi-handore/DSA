def pse(arr):
    st = []
    result = [-1] * len(arr)
    for i in range(len(arr)):
        if st and st[-1] < arr[i]:
            result[i] = st[-1]
        else:
            while st and st[-1] > arr[i]:
                st.pop()
            if not st:
                result[i] = -1
            if st:
                result[i] = st[-1]
        st.append(arr[i])
    return result

if __name__ == '__main__':
    arr = [5, 23, 9, 6, 12, 2, 0, 1]
    print(pse(arr))
