def nextn(n):
    if 2*n < 100:
        return 2*n
    else:
        return (2*n)%100

import numpy as np
def isgood(n):
    ini = n;
    res = [ini]
    while nextn(n) not in res:
        res.append(n)
        n = nextn(n)
#        print(n)

    else:
        if nextn(n) == ini:
            return True
        else:
            return False

#if __name__ == "__main__":
def f(N):
    #T = int(input())
    for i in range(1):
            #N = int(input())
            numgoods = 0
            sumgoods = 0
            j = 10
            while numgoods < N:
                if isgood(j):
                    #print("%d is a good number"%j)
                    numgoods += 1
                    sumgoods += j
                j += 1

            return sumgoods

for i in range(20):
    t = np.random.randint(1,20)
    index = '{0}'.format(str(i).zfill(2))
    fpi = open("Final/in" + index + ".txt" , "w+")
    fpo = open("Final/out" + index + ".txt" , "w+")
    fpi.write(str(t))
    fpi.write(str("\n"))
    for i in range(t):
        temp = np.random.randint(1,20)
        fpi.write(str(temp))
        fpi.write(str("\n"))
        fpo.write(str(f(temp)))
        fpo.write(str("\n"))
    fpi.write(str("\n"))
    fpo.write(str("\n"))
    fpi.close()
    fpo.close()