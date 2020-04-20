
# # списковые включения
# M = [[1,2,3],[4,5,6],[7,8,9]]
# col2 = [row[1] for row in M]
# print(M)
# print(col2)

# # словари
# D ={'word': 4, 'next':0, 'other':3}
# print(D)
#
# rec = {4 : {"name", "lastName"},
#        5 : {"cat", "dont"}}
#
# print(rec[4])
# # восстановление области памяти
# rec = 0
# print(rec)
#
# D = {"a":1,"d":5, "b":2, "c":3}
# Ks = list(D.keys())
# print(Ks)
#
# Ks.sort()
# print(Ks)
#
# for key in Ks:
#     print(key, '=>', D[key])
#
# for c in 'spam':
#     print(c.upper())
#
# squares = [x**2 for x in range(5)]
# print(squares)
#
# squares1 = []
# for x in range(5):
#     squares1.append(x**2)
# print(squares1)
#
# # tuple
# T = (1,2,3,4)
# len(T)
# T = T + (5,6)
#
# print(T[0])
# T[0] = 3
# print(T[0])

# файлы
# f = open('keywords')
# print(f.read())
# f.close()
# for line in open('keywords'): print(line)

# бинарные файлы
import  struct
# packed = struct.pack('>i4sh', 7, b'spam', 8)
# print(packed)
# file = open('data.bin', 'wb')
# file.write(packed)
#
# file.close()

# data = open('data.bin', 'rb').read()
# print(data)
# data[4:8]
# list(data)
# struct.unpack('>i4sh', data)


# unicode файлы
# S = 'sp\xc4m'   #текст unicode, отличный от ascii
# print(S)
#
# file = open('unidata.txt', 'w', encoding='utf-8')
# file.write(S)
# file.close()
#
# text = open('unidata.txt', encoding='utf-8').read()
# print(text)
# len(text)
# list(text)

# raw = open('unidata.txt','rb').read()
# print(raw)
# len(raw)


# # множества
# X = set('spam')
# Y = {'h', 'a', 'm'}
#
# print(X,Y)
# print(X & Y)
# print(X > Y)
#
# A = set(range(4,6))
# B = {3, 5}
# C = X & B
# print(C)

