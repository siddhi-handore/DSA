def towerofHanoi(n, s, h, d):
    if n == 1:
        print(f"Transfer {n} from {s} to {d}")
        return
    towerofHanoi(n-1, s, d, h)
    print(f"Transfer {n} from {s} to {d}")
    towerofHanoi(n-1, h, s, d)

if __name__ == '__main__':
    n = 3
    towerofHanoi(n, "S", "H", "D")