import numpy as np
def rotateList(L, n):
    if n == 0:
        return L
    else:
        return rotateList([L[-1]] + L[:-1], n - 1)
#--
    return res
#print(fibSqrSum(7))

for i in range(20):
    t = np.random.randint(1,100)
    index = '{0}'.format(str(i).zfill(2))
    fpi = open("Final/in" + index + ".txt" , "w+")
    fpo = open("Final/out" + index + ".txt" , "w+")
    fpi.write(str(t))
    fpi.write(str("\n"))
    for i in range(t):
        temp = np.random.randint(1,500)
        k = np.random.randint(1,500)
        fpi.write(str(k))
        fpi.write(str("\n"))
        rand_list = []
        for i in range(temp):
            n = np.random.randint(1,500)
            rand_list.append(n)
            fpi.write(str(n))
            if i < (temp - 1):
                fpi.write(",")
        fpi.write("\n")
        rev_list = rotateList(rand_list, k)
        fpo.write("[")
        for i in range(len(rev_list)):
            fpo.write(str(rev_list[i]))
            if i < len(rev_list) - 1:
                fpo.write(", ")

        fpo.write("]")
        fpo.write("\n")





    #     fpi.write(str(temp))
    #     fpi.write(str("\n"))
    #     fpo.write(str(fibSqrSum(temp)))
    #     fpo.write(str("\n"))
    # fpi.write(str("\n"))
    # fpo.write(str("\n"))
    fpi.close()
    fpo.close()
# for i in range(1000):
#     fpi.write(str(i))
#     fpi.write("\n")
#     fpo.write(str(fibSqrSum(i)))
#     fpo.write("\n")