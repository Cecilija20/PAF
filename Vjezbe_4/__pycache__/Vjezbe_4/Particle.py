import math
import matplotlib.pyplot as plt
class Particle:
    g=-9.81
    def __init__(self,v0,x0,y0,theta,dt=0.01):
        self.t=[]
        self.x=[]
        self.y=[]
        self.vx=[]
        self.vy=[]
        self.ay=[]
        self.vx1=(v0*math.cos(math.radians(theta)))
        self.vx.append(self.vx1)
        self.t.append(0)
        self.dt=dt
        self.vy1=(v0*math.sin(math.radians(theta)))
        self.vy.append(self.vy1)
        self.ay.append(self.g)
        self.x.append(x0)
        self.y.append(y0)
    def reset(self):
        self.t.clear()
        self.vx.clear()
        self.vy.clear()
        self.ay.clear()
        self.y.clear()
        self.x.clear()
    def __move(self,i):
        self.t.append(self.t[i-1]+self.dt)
        self.ay.append(self.g)
        self.vx.append(self.vx1)
        self.vy.append(self.vy[i-1]+self.ay[i]*self.dt)
        self.x.append(self.x[i-1]+self.vx[i]*self.dt)
        self.y.append(self.y[i-1]+self.vy[i]*self.dt)
    def range(self):
        i=0
        while self.y[i]>=0:
            i+=1
            self.__move(i)
        return self.x[i]
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()
        

        

    
        