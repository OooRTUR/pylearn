L = list(range(-5,5))

L1 =list(filter((lambda x: x>-1), L))
print(L1)


[print(x) for x in range(-5,5) if x >=0]