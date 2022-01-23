l=[]
ar=int(input("dwse megethos listas:"))
for i in range(0,ar):
    y=int(input("dwse arithmo gia lista:"))
    l.append(y)

max=l[0]
for i in l:
    if max<i:
        max=i
print(max)
x=0
for i in l:
    if max==i:
        x+=1
for i in range(0,x+1):
    for j in l:
        if max==j:
            l.remove(j)
print(l)
max2=l[0]
for k in l:
    if max2<k:
        max2=k
print(max2)







