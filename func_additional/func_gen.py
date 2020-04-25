def gensquares(N):
    for i in range(N):
        yield i**2

for i in gensquares(5):
    print(i, end=' : ')

x = gensquares(5)
print()
print(x.__next__())
print(next(x))
print(x.__next__())
print(x.__next__())
print(x.__next__())
try:
    print(x.__next__())
except StopIteration:
    print("Iteration stoped")