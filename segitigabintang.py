for i in range(1, 6+1):
    print('  ' * (6 - i), end='')
    for j in range(1, i+1):
        if j == 1:
            print("*", end='')
        else:
            print(" . *", end='')
    print()
