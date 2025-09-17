def longest_consq(arr):
    n = len(arr)
    st = set()

    maxi = 1
    for i in range(n):
        st.add(arr[i])
    for i in st:
        if i - 1 not in st:
            cnt = 1
            x = i
            while x + 1 in st:
                cnt += 1
                x += 1
            maxi = max(cnt, maxi)
    return maxi


if __name__ == '__main__':
    arr = [5, 2, 8, 101, 7, 100, 150, 200, 1, 102, 103, 3]
    print(longest_consq(arr))