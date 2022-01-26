a=[1,2,4]
b=[3,4]
l=[]

for i in a:
    for j in b:
        l1 = []
        l1.append(i)
        l1.append(j)
        t = tuple(l1)
        l.append(t)

print(l)







