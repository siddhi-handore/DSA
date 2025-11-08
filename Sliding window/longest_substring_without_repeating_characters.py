def sub(s):
    n = len(s)
    mp = {}
    l = 0
    maxi = 0
    for j in range(n):
        if s[j] not in mp:
            mp[s[j]] = j
        else:
            if mp[s[j]] >= l:
                l = mp[s[j]] + 1
            mp[s[j]] = j
        length = j-l+1
        maxi = max(length, maxi)
    return maxi

if __name__ == '__main__':
    s = "bbbbbbbb"
    print(sub(s))
