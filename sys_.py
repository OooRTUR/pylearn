import sys

print(sys.executable)
print(sys.argv[1])

if sys.argv[1] == '-v':
    print("Action V")
elif sys.argv[1] == '-d':
    print("Action D")
elif sys.argv[1] == '-e':
    sys.exit(0)
elif sys.argv[1] == 'path':
    print(sys.path)
elif sys.argv[1] == 'add':
    sys.path.append('PycharmProjects/pythonlearn')
    print(sys.path)
elif sys.argv[1] == 'remove':
    sys.path.remove('PycharmProjects/pythonlearn')
    print(sys.path)
elif sys.argv[1] == 'platform':
    print(sys.platform)

print("finished work")