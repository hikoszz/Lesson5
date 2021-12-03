from random import randint
N = 10
a = []
b = []
res1 = []
res2 = []
res3 = []
res4 = []
for i in range(N):
    a.append(randint(1, 10))
    b.append(randint(1, 10))
print(a)
print(b)

for i in a:
    for j in b:        
        if i == j :
            res1.append(i)
print("Входят одновременно в оба - " , set(res1))

for i in a:
  for j in b:
      if  i != j :
        res2.append(i)
print("Входят только в первое, но не входят во второе - " , set(res2))

for i in a:
  for j in b:
      if j != i :
        res3.append(j)
print("Входят только во второе, но не входят в первое - " , set(res3))