for i in range(100):
    if i % 3 == 0:
        print("Three", end="")
    if i % 5 == 0:
        print("Five", end="")
    if i % 3 != 0 and i % 5 != 0:
        print(i, end="")
    print("")
