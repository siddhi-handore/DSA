alpha = "a"
if alpha >= "a" and alpha <= "z":
    num = ord(alpha) - 32
    print(chr(num))

def up(char):
    print(chr(ord(char) & ord(' ')))

if __name__ == '__main__':
    up("a")