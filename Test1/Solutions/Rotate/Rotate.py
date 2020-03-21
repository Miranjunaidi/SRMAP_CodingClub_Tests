


def rotateList(L, n):
    if n == 0:
        return L
    else:
        return rotateList([L[-1]] + L[:-1], n - 1)


if __name__ == "__main__":
    NumTestCases = int(input(""))

    for i in range(NumTestCases):
        n = int(input("")) #number of rotations
        L = [int(elem) for elem in input("").split(",")] #given list
        print(rotateList(L, n))

    
    