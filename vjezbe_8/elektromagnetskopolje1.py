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
    
    def putanja(self, T=30):
        DT = int(T / self.dt)
        i = 0
        while i < DT:
            self.__move(i)
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
