n=int(input("dwse arithmo mathitwn"))
while n<2 or n>10:
    n = int(input("dwse arithmo mathitwn"))
l=[]
for _ in range(0,n):
    on=str(input("dwse onoma"))
    l1=[]
    l1.append(on)
    for j in range(0,3):
        bath=int(input("dwse bathmo"))
        while bath<0 or bath>100:
            bath = int(input("dwse bathmo"))
        l1.append(bath)
    l.append(l1)
print(l)
mol=[]
for i in range(0,n):
    x=0
    mo=0
    for j in range(1,4):
        x+=l[i][j]
    mo=x/3
    print("o "+l[i][0]+" exei mo= "+str(mo))
    mol.append(mo)
print(mol)

for i in range(0,n):
    for j in range(1,4):
        if mol[i]==l[i][j]:
            print(l[i][0])
