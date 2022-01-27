l={}
y=1000
w=0

while True:
    print("1:Dimiourgia Eggrafis\n2:Ektuposi\n3:Enimerosi Eggrafis\n4:Diagrafi Eggrafis\n5:Eksodos")
    x=int(input("dwse tin epilogi sou"))
    egkirotita=0

    if x==5:
        break

    if x==1:
        w+=1
        y+=1
        li=[]
        onoma=str(input("dwse to onoma tou paidiou"))
        eponimo=str(input("dwse to eponimo tou paidiou"))
        patronimo=str(input("dwse to patronimo tou paidiou"))
        for k,v in l.items():
            if onoma in l[k]:
                egkirotita+=1
            if eponimo in l[k]:
                egkirotita+=1
            if patronimo in l[k]:
                egkirotita+=1
        if egkirotita==3:
            print("den ginetai eggrafi edwses ta idia stoixeia me kapoia proigoumenh eggrafi")
            continue
        else:
            li.append(onoma)
            li.append(eponimo)
            li.append(patronimo)

        taksi=int(input("dwse thn taksi tou apo 1-6"))
        while taksi<1 or taksi>6:
            taksi = int(input("dwse thn taksi tou apo 1-6"))
        li.append(taksi)
        l[y]=li

    if x==2:
        print(l)

    if x==3:
        if w==0:

            print("!!! Den uparxei kamia eggrafi !!!")
            continue
        if w!=0:

            lj=[]
            print(f"Oi egrafes einai oi eksis: {l}")
            kod=int(input("dwse egrafi"))
            while kod not in l:
                kod = int(input("dwse egrafi"))
            l.pop(kod)
            onoma = str(input("dwse to onoma tou paidiou"))
            eponimo = str(input("dwse to eponimo tou paidiou"))
            patronimo = str(input("dwse to patronimo tou paidiou"))
            taksi = int(input("dwse thn taksi tou apo 1-6"))
            while taksi < 1 or taksi > 6:
                taksi = int(input("dwse thn taksi tou apo 1-6"))

            lj.append(onoma)
            lj.append(eponimo)
            lj.append(patronimo)
            lj.append(taksi)
            l[kod]=lj

    if x==4:
        if w==0:
            print("!!! Den uparxei kamia eggrafi !!!")
            continue
        if w!=0:
            print(f"Dialekse poia egrafi thes na diagrapseis: {l}")
            kod = int(input("dwse egrafi"))
            while kod not in l:
                kod = int(input("ebales lathos kodiko"))
            l.pop(kod)
            print(f"Oi egrafes eneinan oi eksis: {l}")

print(f"Telos diadikasias oi telikes egrafes einai: {l}")










