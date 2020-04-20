class TestClass:
    data = 0

print(type(TestClass))
print(type([]))

L = []
print(type(L))
test = TestClass
print(type(test))
_type = type(test)
print(_type.__doc__)

if type(L) == type([]):
    print("L is type of []")

if isinstance(L, list):
    print("L is instance")