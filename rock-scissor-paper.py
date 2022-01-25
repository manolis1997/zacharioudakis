import random
p=0
u=0
r=0
lex={}
print("NIKITIS STIS 3 NIKES")
l=["petra","psalidi","xarti"]
print(l)
while True:
    x=int(input("dialekse 0:petra,1:psalidi,2:xarti"))
    print("dialekses: "+str(l[x]))

    y=random.randrange(0,3)
    print("o upologistis pire: "+str(l[y]))
    r+=1
    if x==0:
        if y==1:
            print("kerdise o paikths")
            p+=1
        elif y==2:
            print("kerdise o upo")
            u+=1
        else:
            print("isopalia")

    if x==1:
        if y==0:
            print("kerdise o upo")
            u+=1
        elif y==2:
            print("kerdise o paikths")
            p+=1
        else:
            print("isopalia")

    if x==2:
        if y==0:
            print("kerdise o paikths")
            p+=1
        elif y==1:
            print("kerdise o upo")
            u+=1
        else:
            print("isopalia")
    lex["round",r]="upo:",l[y],"o paikths:",l[x]
    if p==3:
        print("KERDISE O PAIKTHS ME: "+str(p)+ " TON UPO ME :" +str(u))
        break

    if u==3:
        print("KERDISE O UPO ME: "+str(u)+" TON PAIKTH ME: "+str(p))
        break
print(lex)


