def printDiamond(n):
    print("")
    j = 0

    for i in range(0, n):

        for j in range(i, n):
            print("*", end="")

        for j in range(0, 2 * i + 1):
            print(" ", end="")

        for j in range(i, n):
            print("*", end="")

        print("")

    for i in range(0, n - 1):
        for j in range(0, i + 2):
            print("*", end="")

        for j in range(0, 2 * (n - 1 - i) - 1):
            print(" ", end="")

        for j in range(0, i + 2):
            print("*", end="")

        print("")

    print("")


if __name__ == '__main__':
    n = 10
    print("Inverse Diamond Pattern for n = ", n)
    printDiamond(n)

