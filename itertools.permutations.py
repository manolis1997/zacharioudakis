while True:
    s=input("dwse string")
    if s.isupper():
        break
l=[]
for i in s:
    l.append(i)
print(l)

for i in range(len(l)):
    if i==0:
        for j in range(1,len(l)):
            print(f"{l[0]},{l[j]}")

    elif i!=len(l):
        for z in range(0,i):
            print(f"{l[i]},{l[z]}")
        for o in range(len(l)-1,i,-1):
            print(f"{l[i]},{l[o]}")

    else:
        for k in range(len(l)-1,0,-1):
            print(f"{l[i]},{l[k]}")


