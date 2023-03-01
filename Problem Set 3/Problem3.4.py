for beat in range(1, 17):
    if beat % 4 == 1:
        print("B\t", end="")
    elif beat % 4 == 2:
        print("T\t", end="")
    elif beat % 4 == 3:
        print("K\t", end="")
    else:
        print("t\t", end="")