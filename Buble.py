from random import random
a=[]

for i in range(200):
    a.append(int(random()*1000))
print(a)

for i in range(199):
    for j in range(199-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)