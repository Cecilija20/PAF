import matplotlib.pyplot as plt
import numpy as np
import math

def funkcija(x):
    return (x**3)+(2*x**2)+x
def derivacija_funkcije(f,x,h=0.01,metoda=3):
    if metoda==2:
        df=((f(x+h)-f(x)))/h
    elif metoda==3:
        df=((f(x+h)-f(x)))/2*h
    else:
        raise ValueError("Netocna vrijednost metode")
    return df
df=derivacija_funkcije(funkcija,2,metoda=2)




def derivacija_interval(f, a, b, h=0.01, metoda=2): ##a je donja medja,b je gornja medja

    tocke = np.arange(a, b + h, h)
    derivacije = []
    for t in tocke:
       
       derivacija = derivacija_funkcije(f, t, h, metoda)
       derivacije.append(derivacija)
    return tocke, derivacije

a = -5
b = 5
h = 0.1
metoda = 2
x, y = derivacija_interval(funkcija, a, b, h, metoda)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('derivacija')
ax.set_title('Numericka derivacija funkcije ')
plt.show() 





def integral_pravokutna(f, a, b, N): ##a je gornja medja,b je donja medja
    dx = (b - a) / N
    tocke = np.linspace(a, b, N+1)
    sredine = (tocke[1:] + tocke[:-1]) / 2
    vrijednosti = f(sredine)
    donja_meda = np.sum(vrijednosti*dx)
    gornja_meda = np.sum(vrijednosti[::-1]*dx)
    return donja_meda, gornja_meda 
def f(x):
    return x**2

b = 0
a = 1
N = 100

donja_meda, gornja_meda = integral_pravokutna(f, b, a, N)
print("Donja medja 1:", donja_meda)
print("Gornja medja 1:", gornja_meda)

def integral_trapezna(f, a, b, N): ## a je donja,b je gornja
    dx = (b - a) / N
    tocke = np.linspace(a, b, N+1)
    vrijednosti = f(tocke)
    donja_meda = 0
    gornja_meda = 0
    for i in range(N):
        donja_meda += (vrijednosti[i] + vrijednosti[i+1]) * dx / 2
        gornja_meda += (vrijednosti[N-i] + vrijednosti[N-i-1]) * dx / 2
    return donja_meda, gornja_meda
def f(x):
    return x**3
a = 0
b = 1
N = 100
donja_meda, gornja_meda = integral_trapezna(f, a, b, N)
print("Donja meda 2: ", donja_meda)
print("Gornja meda 2: ", gornja_meda)


def trapezna_metoda(f, a, b, n):
    
    h = (b - a) / float(n)

   
    x = [a + i*h for i in range(n+1)]
    y = [f(x[i]) for i in range(n+1)]

    
    integral = (h/2) * (y[0] + y[n] + 2*sum(y[1:n]))

    return integral
def f(x):
    return x**2

integral = trapezna_metoda(f, 0, 1, 10)
print("Numerička vrijednost integrala :", integral)