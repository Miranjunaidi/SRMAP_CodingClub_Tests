import numpy as np
def overlap(L1, L2):
    res = 0
    checked = []
    for elem in L1:
        if (elem in L2) and (elem not in checked):
            res += 1
        checked.append(elem)
    return res

for i in range(20):
    t = np.random.randint(1,100)
    index = '{0}'.format(str(i).zfill(2))
    fpi = open("Final/in" + index + ".txt" , "w+")
    fpo = open("Final/out" + index + ".txt" , "w+")
    fpi.write(str(t))
    fpi.write(str("\n"))
    for i in range(t):
        len_l1 = np.random.randint(1,500)
        len_l2 = np.random.randint(1,500)
        # fpi.write(str(k))
        # fpi.write(str("\n"))
        l1 = []
        l2 = []
        for i in range(len_l1):
            n = np.random.randint(1,500)
            l1.append(n)
            fpi.write(str(n))
            if i < (len_l1 - 1):
                fpi.write(",")
        fpi.write("\n")
        for i in range(len_l2):
            n = np.random.randint(1,500)
            l2.append(n)
            fpi.write(str(n))
            if i < (len_l2 - 1):
                fpi.write(",")
        fpi.write("\n")

        overlap_count = overlap(l1,l2)
        fpo.write(str(overlap_count))
        fpo.write("\n")
    fpi.close()
    fpo.close()