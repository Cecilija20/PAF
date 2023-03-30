import numpy as np
import math

##bez gotovih modula

#aritmeticka sredina:
xi=[1.2,3.4,4.6,2.7,8.9,4.9,7.2,6.6,11.5,28.9]
aritmeticka_s=sum(xi)/len(xi)
print(aritmeticka_s)

##standardna devijacija:
suma=0
xk=[3.5,4.5,5.5,11.5,22.5,15.5,2.7,7.8,9.7,12.5]
a_sredina=sum(xk)/len(xk)
for el in xk:
    a=(el-a_sredina)**2
    suma+=a
s=(suma)/len(xk)
standardna=math.sqrt(s)
print(standardna)

##gotovi moduli

#aritmeticka:
xi1=[1.2,3.4,4.6,2.7,8.9,4.9,7.2,6.6,11.5,28.9]
aritm=np.mean(xi1)
print(aritm)

##standardna devijacija:
xk1=[3.5,4.5,5.5,11.5,22.5,15.5,2.7,7.8,9.7,12.5]
stand=np.std(xk1)
print(stand)






    