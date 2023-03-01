stacks = int(input("How tall should the pyramid be (1-8)? "))

if stacks < 1 or stacks > 8:
    print("The number is out of range.")
else:
    for i in range(stacks):
        print(" " * i + "#" * (stacks - i))