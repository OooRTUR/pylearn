def gen():
    for i in range(10):
        x = yield i
    print(x)

G = gen()

next(G)
next(G)
G.send(77)