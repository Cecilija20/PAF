from harmonic_oscillator import HarmonicOscillator
import matplotlib.pyplot as plt


oscillator = HarmonicOscillator(x0=0.5, v0=0, m=1, k=20, phi=0, dt=0.01)


x, v, a, t = oscillator.oscilacije(10)


print("Analiticki period:", oscillator.analiticki_period())
print("Numericki period:", oscillator.numericki_period())


plt.figure(figsize=(8, 6))
oscillator.plot_xt()

plt.figure(figsize=(8, 6))
oscillator.plot_vt()

plt.figure(figsize=(8, 6))
oscillator.plot_at()





