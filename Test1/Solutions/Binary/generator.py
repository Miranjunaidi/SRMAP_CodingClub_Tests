import numpy as np
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
for i in range(10):
    t = np.random.randint(1,20)
    index = '{0}'.format(str(i).zfill(2))
    fpi = open("Final/in" + index + ".txt" , "w+")
    fpo = open("Final/out" + index + ".txt" , "w+")
    fpi.write(str(t))
    fpi.write("\n")
    for i in range(t):
        n = np.random.randint(6,20)
        pattern = "11011"
        fpi.write(str(n))
        fpi.write("\n")
        fpo.write(str(numsubString(n,pattern)))
        fpo.write("\n")
    fpi.close()
    fpo.close()
