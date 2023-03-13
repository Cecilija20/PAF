import matplotlib.pyplot as plt
import numpy as np


x1_input=input('Unesite x1: ')
try:
    x1 = float(x1_input)
except ValueError:
    print("nije float")

y1_input=input('Unesite y1: ')
try:
    y1 = float(y1_input)
except ValueError:
    print('Nije float')





x2_input=float(input('unesite x2:'))
try:
    x2=float(x2_input)
except ValueError:
    print('nije float')
y2_input=float(input('unesite y2:'))
try:
    y2=float(y2_input)
except ValueError:
    print('nije float')









    


##jednadzba pravca kroz dvije tocke: ##y=((y2-y1)/(x2-x1)*(x-x1))+y1

k=(y2-y1)/(x2-x1)
print(k)
l=y1-k*x1
print(l)

print("y=",k,"x+",l)

def jedn_pravca(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1) 
    a=x2-x1
    if a==0:
        print('nazivnik ne smije biti 0')
    print(k)
    l=y1-k*x1
    print(l)
    print("y=",k,"x +",l)
    return jedn_pravca
jedn_pravca(1.2,1,2.5,3.4)

    

x=np.linspace(x1,x2,10)
y=k*x+l

plt.plot(x,y,'r')
plt.scatter([x1], [y1], color="blue") # plotting single point
plt.scatter([x2], [y2], color="blue") 
plt.show()






