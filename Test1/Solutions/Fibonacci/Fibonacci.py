

def fibSqrSum(n):
    """
    Compute the sum of first n terms in the Fibonacci sequence.

    Input:
    ----------
    n: int
       The number of elements. 
       n >= 0
    Output:
    -------
    out: long 
       The sum of first n terms in the Fibonacci sequence

    >>> fibSqrSum(7)
    104
    >>> fibSqrSum(17)
    1576239
    >>> fibSqrSum(27)
    23843770274
    >>> fibSqrSum(117)
    988894983763579483515701211309921196867143762714
    """
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

print(fibSqrSum(56))

# if __name__ == "__main__":
#     #n = int(input("Give me a number:"))
#     #print(fibSqrSum(n))
#     import doctest
#     doctest.testmod()