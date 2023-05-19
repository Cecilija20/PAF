import numpy as np
import matplotlib.pyplot as plt 
import math
class Projectile:
    g = -9.81

    def __init__(self, v0, x0, y0, theta, ro_zrak=1.22, Cd=1, masa=1, povrsina=0.001, dt=0.01):
        self.t = [0]
        self.vx = [v0 * math.cos(math.radians(theta))]
        self.vy = [v0 * math.sin(math.radians(theta))]
        self.x = [x0]
        self.y = [y0]
        self.m = masa
        self.A = povrsina
        self.CD = Cd
        self.ro = ro_zrak
        self.dt = dt

    def reset(self):
        self.t.clear()
        self.x.clear()
        self.y.clear()
        self.vx.clear()
        self.vy.clear()

    def __moveEuler(self, i):
        self.t.append(self.t[i-1] + self.dt)
        ax = (-0.5 * self.ro * self.CD * self.A * self.vx[i-1] * abs(self.vx[i-1])) / self.m
        ay = self.g + (-0.5 * self.ro * self.CD * self.A * self.vy[i-1] * abs(self.vy[i-1])) / self.m
        self.vx.append(self.vx[i-1] + ax * self.dt)
        self.vy.append(self.vy[i-1] + ay * self.dt)
        self.x.append(self.x[i-1] + self.vx[i] * self.dt)
        self.y.append(self.y[i-1] + self.vy[i] * self.dt)

    def range_Euler(self):
        i = 0
        while self.y[i] >= 0:
            self.__moveEuler(i)
            i += 1
        return self.x, self.y
    

    def __move_runge_kutta(self, i):
        self.t.append(self.t[i-1] + self.dt)
        ax1 = (-0.5 * self.ro * self.CD * self.A * self.vx[i-1] * abs(self.vx[i-1])) / self.m
        ay1 = self.g + (-0.5 * self.ro * self.CD * self.A * self.vy[i-1] * abs(self.vy[i-1])) / self.m
        kx1 = self.vx[i-1]
        ky1 = self.vy[i-1]
        kx2 = self.vx[i-1] + ax1 * (self.dt / 2)
        ky2 = self.vy[i-1] + ay1 * (self.dt / 2)
        ax2 = (-0.5 * self.ro * self.CD * self.A * kx2 * abs(kx2)) / self.m
        ay2 = self.g + (-0.5 * self.ro * self.CD * self.A * ky2 * abs(ky2)) / self.m
        kx3 = self.vx[i-1] + ax2 * (self.dt / 2)
        ky3 = self.vy[i-1] + ay2 * (self.dt / 2)
        ax3 = (-0.5 * self.ro * self.CD * self.A * kx3 * abs(kx3)) / self.m
        ay3 = self.g + (-0.5 * self.ro * self.CD * self.A * ky3 * abs(ky3)) / self.m
        kx4 = self.vx[i-1] + ax3 * self.dt
        ky4 = self.vy[i-1] + ay3 * self.dt
        ax4 = (-0.5 * self.ro * self.CD * self.A * kx4 * abs(kx4)) / self.m
        ay4 = self.g + (-0.5 * self.ro * self.CD * self.A * ky4 * abs(ky4)) / self.m
        self.vx.append(self.vx[i-1] + (self.dt / 6) * (ax1 + 2 * ax2 + 2 * ax3 + ax4))
        self.vy.append(self.vy[i-1] + (self.dt / 6) * (ay1 + 2 * ay2 + 2 * ay3 + ay4))
        self.x.append(self.x[i-1] + (self.dt / 6) * (kx1 + 2 * kx2 + 2 * kx3 + kx4))
        self.y.append(self.y[i-1] + (self.dt / 6) * (ky1 + 2 * ky2 + 2 * ky3 + ky4))


    def plot_trajectory_Euler(self):
        plt.plot(self.x, self.y)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("Euler")
        plt.show()


    def range_runge_kutta(self):
        i = 0
        while self.y[i] >= 0:
            self.__move_runge_kutta(i)
            i += 1
        return self.x, self.y
    
    def plot_trajectory_Runge(self):
        plt.plot(self.x,self.y)
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.title("Runge-Kutta")
        plt.show()
