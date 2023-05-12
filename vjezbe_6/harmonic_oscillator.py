import numpy as np
import matplotlib.pyplot as plt
import math


class HarmonicOscillator:
    def __init__(self, x0=0, v0=0, m=1, k=20, phi=0, dt=0.01):
        self.x = x0
        self.v = v0
        self.m = m
        self.k = k
        self.phi = phi
        self.omega = math.sqrt(self.k / self.m)
        self.t = [0]
        self.x_= [self.x]
        self.v_ = [self.v]
        self.a_ = [(-self.omega ** 2) * self.x]
        self.dt = dt

    def reset(self):
        self.__init__()

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a_.append((-self.omega ** 2) * self.x_[-1])
        self.v_.append(self.v_[-1] + self.a_[-1] * self.dt)
        self.x_.append(self.x_[-1] + self.v_[-1] * self.dt)

    def oscilacije(self, t_max):
        i_max = int(t_max / self.dt)
        for i in range(i_max):
            self.__move()
        return self.x_, self.v_, self.a_, self.t

    def analiticki_period(self):
        return 2 * math.pi * math.sqrt(self.m / self.k)

    def numericki_period(self):
        T = 0
        while self.x_[-1] >= self.x:
            self.__move()
            T += self.dt
        return 2 * T

    def plot_xt(self):
        plt.plot(self.t, self.x_)
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.title("x-t")
        plt.show()

    def plot_vt(self):
        plt.plot(self.t, self.v_)
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]")
        plt.title("v-t")
        plt.show()

    def plot_at(self):
        plt.plot(self.t, self.a_)
        plt.xlabel("t [s]")
        plt.ylabel("a [m/s^2]")
        plt.title("a-t")
        plt.show()
