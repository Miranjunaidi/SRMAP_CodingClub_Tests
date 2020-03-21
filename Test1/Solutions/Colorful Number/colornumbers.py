

# reds = set([i for i in range(1001) if i%5 == 0])
# blues = set([i for i in range(1001) if i%3 == 0])

# left_reds = reds - blues
# final_reds = [i for i in left_reds if (i%14 != 0)]


# print(sum(final_reds))


i = 0
res = 0
N = int(input())
while i <= N:
    if (i%5 == 0) and (i%3 != 0) and (i%14 != 0):
        res += i

    i += 1

print(res)
        
