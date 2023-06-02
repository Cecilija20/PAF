import numpy as np
import math
import matplotlib.pyplot as plt
class Gravitacija:
    def __init__(self,m1, m2, r1, r2, v1, v2, konstanta = 6.67*(10**(-11)), t0=0, dt = 86400):
        self.x1 = []
        self.x2 = []
        self.y1 = []
        self.y2 = []
        self.t = t0
        self.M = m1
        self.m = m2
        self.R = r1
        self.r = r2
        self.V = v1
        self.v = v2
        self.G = konstanta
        self.dt = dt
        self.x1.append(self.R[0])
        self.y1.append(self.R[1])
        self.x2.append(self.r[0])
        self.y2.append(self.r[1])
    def reset(self):
        self.x1.clear()
        self.x2.clear()
        self.y1.clear()
        self.y2.clear()
    def move(self, T):
        while self.t < T:
            Rr = math.sqrt((self.R[0]-self.r[0])**2 + (self.R[1]-self.r[1])**2)
            rR = math.sqrt((self.r[0]-self.R[0])**2 + (self.r[1]-self.R[1])**2)
            A = -(self.G*self.m)/(Rr**3)*np.subtract(self.R, self.r)
            a = -(self.G*self.M)/(rR**3)*np.subtract(self.r, self.R)
            self.V = np.add(self.V, A*self.dt)
            self.v = np.add(self.v, a*self.dt)
            self.R = np.add(self.R, self.V*self.dt)
            self.r = np.add(self.r, self.v*self.dt)
            self.x1.append(self.R[0])
            self.x2.append(self.r[0])
            self.y1.append(self.R[1])
            self.y2.append(self.r[1])
            self.t += self.dt
        return self.x1, self.y1, self.x2, self.y2
        

    
Sunce = 1.989e30
Zemlja = 5.967e24
R = np.array((0.,0.))
AJ= 1.486e11
r=  np.array((AJ,0))
V = np.array((0.,0.))
v = np.array((0,29783))
sz = Gravitacija(Sunce,Zemlja,R,r,V,v,konstanta=6.67*10**(-11),t0=0,dt=86400)
T = 60*60*24*365
X,Y,x,y = sz.move(T)
ax = plt.axes()
plt.plot(X,Y,"yo")
plt.plot(x,y,"blue")
plt.show()  