import numpy as np
def deciToTeri(n):
    res = " "
    while True:
        res = str(n % 3) + res
        n = n//3
        if n == 0:
            return res
for i in range(20):
    t = np.random.randint(1,20)
    index = '{0}'.format(str(i).zfill(2))
    fpi = open("Final/in" + index + ".txt" , "w+")
    fpo = open("Final/out" + index + ".txt" , "w+")
    fpi.write(str(t))
    fpi.write("\n")
    for i in range(t):
        n = np.random.randint(1,10000)
        pattern = "11011"
        fpi.write(str(n))
        fpi.write("\n")
        fpo.write(str(deciToTeri(n)))
        fpo.write("\n")
    fpi.close()
    fpo.close()
