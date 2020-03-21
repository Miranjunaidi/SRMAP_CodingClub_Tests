

def all_n_BinStrings(n):
    if n == 1:
        return ["0", "1"]
    else:
        given = all_n_BinStrings(n-1)
        res = []
        for bistr in given:
            res.append(bistr + '0')
            res.append(bistr + '1')
        return res

def numsubString(n, pattern):
    return sum([(pattern in s) for s in all_n_BinStrings(n)])

#print(numsubString(6, "11011"))

if __name__ == "__main__":
    NumTestCases = int(input())
    for i in range(NumTestCases):
        n = int(input(""))
        pattern = "110011"
        print(numsubString(n, pattern))

