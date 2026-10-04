for x in "0123456789abcdefg":
    v = int(f"29765{x}43", 17) + int(f"21{x}14", 17)
    if v % 16 == 0:
        print(v // 16)
        break