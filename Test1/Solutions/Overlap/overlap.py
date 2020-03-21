


def overlap(L1, L2):
    res = 0
    checked = []
    for elem in L1:
        if (elem in L2) and (elem not in checked):
            res += 1
        checked.append(elem)
    return res
    


if __name__ == "__main__":
    NumTestCases = int(input())
    for case in range(NumTestCases):
        L1 = [int(e) for e in input().split(",")]
        L2 = [int(e) for e in input().split(",")]
    
        print(overlap(L1, L2))