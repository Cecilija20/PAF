import Particle as par
import matplotlib.pyplot as plt
import math
r_greska=[]
Dt=[]
dt1=0.001
p_1=par.Particle(10,0,0,60,0.001)

D=(10**2)*math.sin(math.radians(120))/9.81
print("Analitički domet je {} m, ,numerički je {} m".format(round(D,3),round(p_1.range(),3)))
p_1.range()
p_2=par.Particle(10,0,0,60,0.001)
for i in range(0,100):
    dt1+=0.001
    Dt.append(dt1)
for dt in Dt:
    p_2=par.Particle(10,0,0,60,dt)
    greska=((abs(p_2.range()-D)/D))*100
    r_greska.append(greska)
    p_2.reset()
plt.plot(Dt,r_greska)
plt.xlabel("dt [s]")
plt.ylabel("Relativna greska")
plt.title("Ovisnost relativne greške računanja u odnosu na dt interval")
plt.show()


