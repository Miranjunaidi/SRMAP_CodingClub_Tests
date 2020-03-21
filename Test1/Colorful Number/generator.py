import numpy as np
def colourfulsum(N):	
	i = 0
	res = 0
	while i <= N:
	    if (i%5 == 0) and (i%3 != 0) and (i%14 != 0):
	        res += i

	    i += 1

	return res



for i in range(20):
    t = np.random.randint(1,100)
    index = '{0}'.format(str(i).zfill(2))
    fpi = open("Final/in" + index + ".txt" , "w+")
    fpo = open("Final/out" + index + ".txt" , "w+")
    fpi.write(str(t))
    fpi.write(str("\n"))
    for i in range(t):
        temp = np.random.randint(1,10000)
        fpi.write(str(temp))
        fpi.write(str("\n"))
        fpo.write(str(colourfulsum(temp)))
        fpo.write(str("\n"))
    fpi.write(str("\n"))
    fpo.write(str("\n"))
    fpi.close()
    fpo.close()