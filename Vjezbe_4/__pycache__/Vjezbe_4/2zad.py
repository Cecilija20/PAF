import math
import matplotlib.pyplot as plt
import numpy as np
import Particle as par
def izračunaj_grešku_domet(dt):
    p = par.Particle(10,0,0,60,dt)
    analiticki_domet = (10**2)*math.sin(math.radians(120))/9.81
    numericki_domet = p.range()
    greska = abs(analiticki_domet - numericki_domet) / analiticki_domet * 100
    p.reset()
    return greska

dt_vrijednosti = []
relativna_greska = []

for i in range(1, 101):

    dt = i / 1000
    dt_vrijednosti.append(dt)
    greska = izračunaj_grešku_domet(dt)
    relativna_greska.append(greska)

plt.plot(dt_vrijednosti, relativna_greska)
plt.xlabel("dt [s]")
plt.ylabel("Relativna greška")
plt.title("Ovisnost relativne greške računanja u odnosu na dt interval")
plt.show()






