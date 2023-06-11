import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class ElektroMagnetskoPolje:
    def __init__(self, x0, y0, z0, v0, m, Q, elektricno_polje, magnetsko_polje, dt=0.01):
        self.x = []
        self.y = []
        self.z = []
        self.v = v0
        self.m = m
        self.x.append(x0)
        self.y.append(y0)
        self.z.append(z0)
        self.q = Q
        self.E = elektricno_polje
        self.B = magnetsko_polje
        self.a = np.array((0, 0, 0))
        self.dt = dt
    
    def reset(self):
        self.x.clear()
        self.y.clear()
        self.z.clear()
    
    def __move(self, i):
        self.a = (self.q) * (self.E + np.cross(self.v, self.B) / self.m)
        self.v = self.v + self.a * self.dt
        self.x.append(self.x[i - 1] + self.v[0] * self.dt)
        self.y.append(self.y[i - 1] + self.v[1] * self.dt)
        self.z.append(self.z[i - 1] + self.v[2] * self.dt)

    def __moverungekutta(self,i):
        v1=(self.q/self.m)*(self.E+np.cross(self.v,self.B)*self.dt)
        r1=(self.v)*self.dt
        v2=(self.q/self.m)*(self.E+np.cross(self.v+v1/2,self.B)*self.dt)
        r2=(self.v+v1/2)*self.dt
        v3=(self.q/self.m)*(self.E+np.cross(self.v+v2/2,self.B)*self.dt)
        r3=(self.v+v2/2)*self.dt
        v4=(self.q/self.m)*(self.E+np.cross(self.v+v3/2,self.B)*self.dt)
        r4=(self.v+v3/2)*self.dt
        self.v=self.v+(v1+2*v2+2*v3+v4)/6
        self.x.append(self.x[i-1]+(r1[0]+2*r2[0]+2*r3[0]+r4[0])/6)
        self.y.append(self.y[i-1]+(r1[1]+2*r2[1]+2*r3[1]+r4[1])/6)
        self.z.append(self.z[i-1]+(r1[2]+2*r2[2]+2*r3[2]+r4[2])/6)


    
    
    def putanja(self, T=30):
        DT = int(T / self.dt)
        i = 0
        while i < DT:
            self.__move(i)
            i += 1
        return self.x, self.y, self.z
    
    def putanja_rungekutta(self, T=30):
        DT = int(T / self.dt)
        i = 0
        while i < DT:
            self.__moverungekutta(i)
            i += 1
        return self.x, self.y, self.z
    
    
p1 = ElektroMagnetskoPolje(0, 0, 0, np.array((0.1, 0.1, 0.1)), 1, 1, np.array((0, 0, 0)), np.array((0, 0, 1))) #pozitron
p2 = ElektroMagnetskoPolje(0, 0, 0, np.array((0.1, 0.1, 0.1)), 1, -1, np.array((0, 0, 0)), np.array((0, 0, 1))) #elektron

x1, y1, z1 = p1.putanja(50)
x2, y2, z2 = p2.putanja(50)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x1, y1, z1, c="r", label="pozitron")
ax.plot3D(x2, y2, z2, c="b", label="elektron")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("z [m]")
ax.set_title("Usporedba gibanja elektrona i pozitrona u konstantnom magnetskom polju")
ax.legend()
plt.show()

p1.reset()
p2.reset()


prk1=ElektroMagnetskoPolje(0, 0, 0, np.array((0.1, 0.1, 0.1)), 1, -1, np.array((0, 0, 0)), np.array((0, 0, 1)))
prk2=ElektroMagnetskoPolje(0, 0, 0, np.array((0.1, 0.1, 0.1)), 1, -1, np.array((0, 0, 0)), np.array((0, 0, 1)))
x1,y1,z1=prk1.putanja()
x2,y2,z2=prk2.putanja_rungekutta()
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot(x1,y1,z1,"blue",label="Euler")
ax.plot(x2,y2,z2,"red",label="Runge-Kutta")
ax.set_xlabel("x[m]")
ax.set_ylabel("y[m]")
ax.set_zlabel("z[m]")
ax.set_title("Usporedba putanje elektrona  Runge-Kutta i Euler metodom")
ax.legend(["Euler","Runge-Kutta"])
plt.show()
prk1.reset()
prk2.reset()