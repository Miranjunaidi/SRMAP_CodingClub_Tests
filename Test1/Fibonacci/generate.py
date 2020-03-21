import numpy as np
def fibSqrSum(n):
    a = 0; b = 1;
    res = a*a
    i = 0
    while i < n:
        res += a*a
#--
        temp = b
        b = a + b
        a = temp
        i += 1
#--
    return res
#print(fibSqrSum(7))

for i in range(20):
    t = np.random.randint(1,100)
    index = '{0}'.format(str(i).zfill(2))
    fpi = open("in" + index + ".txt" , "w+")
    fpo = open("out" + index + ".txt" , "w+")
    fpi.write(str(t))
    fpi.write(str("\n"))
    for i in range(t):
        temp = np.random.randint(1,100)
        fpi.write(str(temp))
        fpi.write(str("\n"))
        fpo.write(str(fibSqrSum(temp)))
        fpo.write(str("\n"))
    fpi.write(str("\n"))
    fpo.write(str("\n"))
    fpi.close()
    fpo.close()
# for i in range(1000):
#     fpi.write(str(i))
#     fpi.write("\n")
#     fpo.write(str(fibSqrSum(i)))
#     fpo.write("\n")