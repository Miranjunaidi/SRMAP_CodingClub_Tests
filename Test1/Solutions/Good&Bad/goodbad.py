
def nextn(n):
    if 2*n < 100:
        return 2*n
    else:
        return (2*n)%100
    
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
    
if __name__ == "__main__":
    N = int(input())

    numgoods = 0
    sumgoods = 0
    j = 0
    while numgoods < N:
        if isgood(j):
            print("%d is a good number"%j)
            numgoods += 1
            sumgoods += j
        j += 1
            
    print(sumgoods)

