def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state+=1
    return nested

F = tester(0)
F('spam')
F('Ham')
F('eggs')

class Tester:
    def __init__(self,start):
        self.__state = start
    def __call__(self, label):
        print(label, self.__state)
        self.__state+=1
    def get_state(self):
        return  self.__state

H = Tester(99)
H('juice')
H('single')
print(H.get_state())

import builtins

def makeopen(id):
    original = builtins.open
    def custom(*pargs, **kargs):
        print('Custom open call %r'%id, pargs, kargs)
        return original(*pargs, **kargs)
    builtins.open = custom

F = open('data.json')
F.read()
print(F)

makeopen('custom')
F = open('data.json')
F.read()
