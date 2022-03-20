x=int(input("dwse arithmako eggrafwn:"))
l=[]
for i in range(0,x):
    n=str(input("dwse onomataki mathitou:"))
    b=int(input("dwse bathmo mathitou"))
    l1=[]
    l1.append(n)
    l1.append(b)
    l.append(l1)
print(l)
min=l[0][1]
for i in range(0,x):
    if min>l[i][1]:
        min=l[i][1]
print(min)





