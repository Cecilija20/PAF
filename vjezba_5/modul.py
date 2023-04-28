import calculus as cal
import math
import numpy as np
import matplotlib.pyplot as plt

a = -5
b = 5
ep = 0.01
metoda = 3
x, y = cal.derivacija_interval(cal.funkcija, a, b, ep, metoda)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('derivacija')
ax.set_title('Numericka derivacija funkcije ')
plt.show() 

##analiticko rjesenje:
def fun(x):
    return (x**3)+(2*x**2)+x

x_analiticko=np.linspace(a,b,1000)
y_analiticko=(3*(x_analiticko**2)+(2*(x_analiticko)**2))

##numericko
x_numericko,y_numericko=cal.derivacija_interval(cal.funkcija,a,b,ep)


fig,ax=plt.subplots()
ax.plot(x_analiticko,y_analiticko,label="Analiticko rjesenje")
ax.plot(x_numericko,y_numericko,label="Numericko rjesenje")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
plt.show()












