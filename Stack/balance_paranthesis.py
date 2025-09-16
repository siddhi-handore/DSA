def check_balance(s):
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == "{":
            st.append(s[i])
        else:
            if not st:
                return False
            ch = st.pop()
            if (s[i] == ')' and ch != '(') or (s[i] == ']' and ch != '[') or (s[i] == '}' and ch != '{'):
                return False
    return True

s = "()[{}()]"
print(check_balance(s))