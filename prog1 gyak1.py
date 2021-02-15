# 1---------------

# n=int(input("adj meg egy szamot"))
# while n!=0:
#     if n%2==0:
#         print(n+"páros szám")
#     else:
#         print(n+"páratlan szám")
#     n = int(input("adj meg egy szamot"))

# 2----------------

# def GCD(a,b):
#     if a>b:
#         tmp=a
#         a=b
#         b=tmp
#         b=tmp
#         #  a,b=b,a
#     res=1
#     for i in range(2,a+1):
#         if a%i==0 and b%i==0:
#             res=i
#     return res
#
#
# #MAIN:
# a=int(input("Adja meg az első számot"))
# b=int(input("Adja meg az masodik számot"))
# res =GCD(a,b)
# print("{} szam és {} stam legnagyobb közös osztója: {}".format(a,b,res))

# 3---------------

# import math
# x1=int(input("Adja meg az a első koordinátáját"))
# y1=int(input("Adja meg az a masodik koordinátáját"))
# x2=int(input("Adja meg az b első koordinátáját"))
# y2=int(input("Adja meg az b masodik koordinátáját"))
# x=(x2-x1)**2
# y=(y2-y1)**2
# tav=math.sqrt(x+y)
# print("a két vektor távolsága",tav)

# 4----------------

# sum=0
# n=input("Adj meg egy számot")
# lista=list(n)
# for i in lista:
#     a=int(i)
#     sum+=a
# print(sum)

# 5----------------

# szavak=input("adj meg szavakat vesszővel elválasztva")
# lista=[]
# lista=szavak.split(",")
# lista.sort()
# uj=[]
# for i in lista:
#     if i not in uj:
#         uj.append(i)
# uj.sort()
# print(uj)

# 6----------------

# n=int(input("adj meg egy számot"))
# szöveg=input("adj meg egy szöveget")
# hossz=len(szöveg)
# if hossz<n:
#     print(szöveg)
# else:
#     print(szöveg[0:n])