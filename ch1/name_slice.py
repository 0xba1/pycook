# Naming a Slice

def main():
    a = "a|12|b|55"
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    SLICE1 = slice(2, 4) # (start, stop)
    SLICE2 = slice(2, 8, 2) # (start, stop, step)

    print(a[2:4]) # 17
    print(a[SLICE1]) # 17
    print(b[2:8:2]) # [3, 5, 7]
    print(b[SLICE2]) # [3, 5, 7]


if __name__ == "__main__":
    main()
