l=["amaksi","kados","kinito","othoni","trapezi","paixnidi","grafeio","eikona","potiri","tsanta","tetradio"]
x=int(input("dwse arithmo 0-10"))
hw=l[x]
mikos=0
emf_leksis=[]
for _ in range(len(hw)):
    emf_leksis.append("_")
print(emf_leksis)
max=10


while mikos<len(hw) and max>0:
    print(f"exeis {max} eukairies na breis tin leksi")
    g=input("dwse gramma")
    guessed_letter=[]
    guessed_letter.append(g)

    emfanisi=0
    for i in hw:
        if i==g:
            mikos+=1
            emfanisi+=1
    print(f"exei emfanistei to {g} gramma {emfanisi} fores")
    x=0
    for i in hw:
        if i==g:
            emf_leksis[x]=g
        x+=1
    print(emf_leksis)
    max-=1
    print(f"exeis akoma {max} fores")

if max>0:
    print(f"brikes thn leksi {hw}")
else:
    print(f"den brikes thn leksi pou itan {hw}")












