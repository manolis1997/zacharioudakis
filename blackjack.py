import random

def xarti():
    z=random.randrange(0,12)
    return z


l=[1,2,3,4,5,6,7,8,9,10,"K","Q","J"]
skor=0
skorupo=0

x=random.randrange(0,12)
y=random.randrange(0,12)
print(x,y)

if x>=0 and x<=9:
    skor=skor+x
    print(skor)
else:
    skor=skor+10
    print(skor)
if y>=0 and y<=9:
    skor=skor+y
    print(skor)
else:
    skor=skor+10
    print(skor)


while True:
    print("thes na sunexiseis nai h oxi?")
    apant=str(input("dwse ap"))

    if apant=="oxi":
        print("stamatises sto "+str(skor))
        break
    else:
        skor=skor+xarti()
        print(skor)
    if skor>21:
        print("exases")
        break
    if skor==21:
        print("magka tous gamises")
        break

print("twra paizei o upo")
while True:
    u=random.randrange(0,12)
    skorupo=skorupo+u
    print(skorupo)
    if skorupo>21:
        print("exase o upo")
        break
    if skorupo>=skor:
        print("kerise o upo")
        break















