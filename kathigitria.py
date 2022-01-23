import random

while True:
    p = random.randrange(2, 10)
    if p % 2 == 0:
        break
print("ta paidia einai: "+str(p))
for _ in range(2):
    i=0
    l=[]
    while i<p/2:
        while True:
            x = random.randrange(0, p)
            if x not in l:
                l.append(x)
                break


        while True:
            y = random.randrange(0, p)
            if y not in l:
                l.append(y)
                break
        i+=1

    print(l)













