import matplotlib.pyplot as plt
import numpy as np
import math

def kosi_hitac(v0,kut):
    vx1=v0*math.cos(math.radians(kut))
    vy1=v0*math.sin(math.radians(kut))
    g=9.81
    x0=0
    y0=0
    t0=0
    dt=0.01
    x=[]
    y=[]
    t=[]
    for e in range(0,1000):
        t0=dt*e
        t.append(t0)
        x0=x0+vx1*dt
        x.append(x0)
        vy1=vy1-g*dt
        y0=y0+vy1*dt
        y.append(y0)
    
    plt.plot(x,y)
    plt.title("x-y graf")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.show()

    
    plt.plot(t,x)
    plt.title("x-t graf")
    plt.xlabel("vrijeme(t [s])")
    plt.ylabel("x [m]")
    plt.show()

    plt.plot(t,y)
    plt.title("y-t graf")
    plt.xlabel("vrijeme(t [s])")
    plt.ylabel("y [m]")
    plt.show()
    
    
    return gibanje2
kosi_hitac(100,20)
   