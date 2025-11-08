def convert(char):
    print(chr(ord(char) ^ ord(' ')))

if __name__ == '__main__':
    convert("a")
    convert("B")