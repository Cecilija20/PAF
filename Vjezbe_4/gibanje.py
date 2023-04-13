import Particle as par
import matplotlib.pyplot as plt
import math
p_1=par.Particle(10,0,0,60,0.001)

d=(10**2)*math.sin(math.radians(120))/(9.81)
print("domet kosog hica izračunat analitički je {} m , a numerički {} m.".format(round(d,3),round(p_1.range(),3)))
p_1.range()
p_1.plot_trajectory()
p_1.reset()
