import matplotlib.pyplot as plt
import numpy as np


def gibanje(F,m):
    a1=F/m
    x0=0
    v0=0
    t0=0
    dt=0.01
    x=[]
    v=[]
    t=[]
    a=[]
    for e in range(0,1000):
        a.append(a1)
        t0=dt*e
        t.append(t0)
        v0=v0+a1*dt
        v.append(v0)
        x0=x0+v0*dt
        x.append(x0)
    plt.plot(t,x)
    plt.xlabel("t [s]")
    plt.ylabel("x [m]")
    plt.show()
    plt.plot(t,v)
    plt.xlabel("t [s]")
    plt.ylabel("v [m/s]")
    plt.show()
    plt.plot(t,a)
    plt.xlabel(" t [s]")
    plt.ylabel("a [m/s2]")
    plt.show()
    return gibanje
gibanje(30,50)