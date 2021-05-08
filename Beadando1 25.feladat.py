import numpy as np
n=int(input("Adj meg egy számot  "))
k=int(input("Adja meg a vektor intervallumának kezdőértékét  "))
v=int(input("Adja meg a vektor intervallumának végértékét  "))
m=int(input("Adja meg a vektor méretét  "))
print('  ')
lista=[]

def osszefuz(szamoklista,muveletlista):
    szoveg=""
    # print(szamoklista)
    # print(muveletlista)
    for i in range(len(szamoklista)):
        szoveg=szoveg+str(szamoklista[i])+muveletlista[i]
    szoveg=szoveg[:-1]
    # print(szoveg)
    return ([szoveg,eval(szoveg)])



for i in range(0,n):
    vektor=np.random.randint(k,v,m)
    lista.append(vektor)
    # print (vektor)



    for item in lista:
        primlista = []
        paroslista = []
        paratlanlista = []
        muveletlista = []
        db = 0
        paros = 0
        paratlan = 0
        for szam in item:
            flag = False
            if szam > 1:
                for j in range(2, szam):
                    if (szam % j) == 0:
                        flag = True
                        break
                if not flag:
                    db += 1
                    primlista.append(szam)

            if szam%2==0:
                paros+=1
                paroslista.append(szam)

            else:
                paratlan+=1
                paratlanlista.append(szam)
    print('  ')
    # print(db,'ennyi db prim van')
    # print(primlista, "primszamok  ")
    # print('  ')
    #print(paros,'ennyi db paros van')
    # print(paroslista,"parosszamok  ")
    # print('  ')
    #print(paratlan,'ennyi db paratlan van')
    # print(paratlanlista,"paratlanszámok  ")
    # print('  ')
    # print(lista)
    # print('  ')


    if db>=2:
        for asd in range(0, db):

            jel = np.random.randint(0, 4)
            muvelet = ''
            if jel == 0:
                muvelet = '-'
            elif jel == 1:
                muvelet = '+'
            elif jel == 2:
                muvelet = '*'
            elif jel == 3:
                muvelet = '/'
            muveletlista.append(muvelet)
        print(f"{i+1}. (Prím számok) {osszefuz(primlista,muveletlista)[0]} = {round(osszefuz(primlista, muveletlista)[1],2)}")
        #primszamokra
    elif db<2:
        if paratlan>=2:
            for asd in range(0, paratlan ):
                jel = np.random.randint(0, 4)
                muvelet = ''
                if jel == 0:
                    muvelet = '-'
                elif jel == 1:
                    muvelet = '+'
                elif jel == 2:
                    muvelet = '*'
                elif jel == 3:
                    muvelet = '/'
                muveletlista.append(muvelet)
            print(f"{i+1}. (Paratlan számok) {osszefuz(paratlanlista,muveletlista)[0]} = {round(osszefuz(paratlanlista, muveletlista)[1],2)}")
            # akkorpáratlan számokra kell elvégezni a generált számokat
        elif paratlan<2:
            for asd in range(0, paros):
                jel = np.random.randint(0, 4)
                muvelet = ''
                if jel == 0:
                    muvelet = '-'
                elif jel == 1:
                    muvelet = '+'
                elif jel == 2:
                    muvelet = '*'
                elif jel == 3:
                    muvelet = '/'
                muveletlista.append(muvelet)
            print(f"{i+1}. (Páros számok) {osszefuz(paroslista,muveletlista)[0]} = {round(osszefuz(paroslista, muveletlista)[1],2)}")
# print(muveletlista)
