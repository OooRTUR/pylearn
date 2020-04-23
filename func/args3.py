def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return  res

def min2(first, *rest):
    for arg in rest:
        if arg <first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


L = [5,6,25,3,-1,-15]
print(min(*L))
print(min2(*L))
print(min3(*L))