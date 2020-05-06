def mysum(L):
    return  0 if not L else L[0] + mysum(L[1:])

print(mysum([1,2,3,4,5]))

def func(a: int, b:int, c:int) -> int:
    return  a + b +c

func(4, 2, 3)
print(func.__annotations__)