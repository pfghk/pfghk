import xlrd
import matplotlib.pyplot as plt


loc=("telepek.xls")

wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)

sheet.cell_value(0,0)

print(sheet.row_values(0))
for i in range(1,len(sheet.row(0))):
    sorlista=[]
    for j in range(len(sheet.row_values(i))):
        if j <=i:
            if sheet.row_values(i)[j]=='':
                sorlista.append(0)
            else:
                sorlista.append(sheet.row_values(i)[j])
    print(sorlista)

nepesseg=[["Budapest",1750000],["Debrecen",201000],["Szeged",160000],["Miskolc",153000],["Pécs",141000],["Győr",133000],["Nyíregyháza",116000],["Kecsekmét",110000],["Székesfehérvár",97000],["Szombathely",78000],["Szolnok",70000],["Tatabánya",66000],["Kaposvár",60000],["Veszprém",60000],["Békéscsaba",58000],["Zalaegerszeg",56000],["Eger",51000],["Salgótarján",33000],["Szekszárd",31000]]
nepesseg.sort(key=lambda x: x[1], reverse=True)

varosok=[]
for i in range(len(nepesseg)):
    varosok.append(nepesseg[i][0])
print(varosok)

lakossag=[]
for i in range(len(nepesseg)):
    lakossag.append(nepesseg[i][1]/700)
print(lakossag)


y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
plt.xticks(rotation='vertical')
plt.scatter(varosok,y,s=lakossag)
plt.show()