from functools import reduce
import operator

reduce((lambda x,y: x+y), [1,2,3,4])

res = reduce((lambda x,y: x*y), range(1,12))
print(res)

res = reduce(operator.add, range(4))
print(res)