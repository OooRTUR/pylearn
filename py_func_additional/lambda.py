f = lambda x,y,z : x + y + z
print(f(2,3,4))
print(type(f))

L = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

for f in L:
    print(f(2))

t = L[0](3)
print(t)