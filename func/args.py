def func(x):
    x+=1
    print(x)

c = 5
func(c)
print(c)

def charge(a,b):
    a = 2
    b[0] = 'spam'
    return  a,b

L = [1,2]
x= 1
print(charge(x, L[:]))
print(x, L)


