class stack:

    def __init__(self):
        self.st = []
        self.minElem = float('inf')

    def push(self, val):
        if not self.st:
            self.minElem = val
            self.st.append(val)
        if val < self.minElem:
            self.st.append(2 * val - self.minElem)
            self.minElem = val
        else:
            self.st.append(val)

    def pop(self):
        if not self.st:
            return
        top = self.st.pop()
        if top < self.minElem:
            self.minElem = 2 * self.minElem - top
        return top

    def peek(self):
        if not self.st:
            return -1
        top = self.st[-1]
        return self.minElem if self.minElem > top else top

    def getMin(self):
        if not self.st:
            return -1
        return self.minElem

if __name__ == '__main__':
    st = stack()
    st.push(3)
    st.push(8)
    st.push(2)
    st.push(-4)
    print(f" Min elem = {st.getMin()}")
    print(f" Pop elem = {st.pop()}")
    print(f" Min elem = {st.getMin()}")


