def f (a,b=15,c=31) : print(a,b,c)

f(1,2,3)

f(a=2, b=1,c=3)

f(2)

def f1(*args) :
    print(args)
    print(type(args))
f1(1,2,3,4)

def f2(**args): print(args); print(type(args))

f2(t=1, b=2)

def f3(a, *args, **kargs): print(a, args, kargs)

f3(1,2,3, x=1, y=2)

def f4(a,b,c,d): print(a,b,c,d)

args = (1,2)
args +=(3,4)
print(args)
f4(*args)
