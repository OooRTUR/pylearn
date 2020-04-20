import  json

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev','mgr'], age=40.5)
print(rec)

json.dumps(rec)
S = json.dumps(rec)
print(S)
print(type(S))

json.dump(rec, fp=open('testjson.txt', 'w'),indent=4)
print(open('testjson.txt').read())
P = json.load(open('testjson.txt'))
print(P)