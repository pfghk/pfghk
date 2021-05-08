import matplotlib.pyplot as plt

fin=open("input.txt","r")
# fout=open("output.txt","w")

allergenek=["gluten","mogyoro","magvak","zeller","mustar","tojas","tej","szezammag","hal","rak","kagylo","szoja","szulfatok","huvelyesek"]
allergenekszamokkal=[]
for i in range(len(allergenek)):
    allergenekszamokkal.append([allergenek[i],0])

osszetevok=input("Adja meg az összetvőket vesszővel elválasztva, szóköz nélkül: ")

listaösszetevok=osszetevok.split(",")
for i in listaösszetevok:
    for j in range(len(allergenekszamokkal)):
        if i==allergenekszamokkal[j][0]:
            allergenekszamokkal[j][1]+=1
print(allergenekszamokkal)

csakszamok=[]
for i in range(len(allergenekszamokkal)):
    csakszamok.append(allergenekszamokkal[i][1])


#gluten,gluten,mogyoro,gluten,gluten,mogyoro,magvak,zeller,mustar,szezammag,rak,hal,hal,hal,kagylo,tej,zeller,tojas,tojas,tojas,tej,gluten,tej,zeller,tojas,tojas,tojas,tej,gluten
szinek=[]
for sor in fin:
    sor=sor.strip()
    if sor[0]=="+":
        szinek.append("red")
    else:
        szinek.append("green")

# for i in range(len(allergenekszamokkal)):
#     print(f"{allergenekszamokkal[i][0]} anyagbol {allergenekszamokkal[i][1]} db van az osszetevokben",file=fout)
fin.close()
# fout.close()

plt.xticks(rotation='vertical')
plt.bar(allergenek, csakszamok,color=szinek)
plt.savefig('kep.png',bbox_inches='tight')
plt.show()