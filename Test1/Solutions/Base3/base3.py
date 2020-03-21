def deciToTeri(n):
    res = " "
    while True:
        res = str(n % 3) + res
        n = n//3
        if n == 0:
            return res


if _name_ == "_main_":
    T = int(input())
    for i in range(T):
        n = int(input())
        print(deciToTeri(n))