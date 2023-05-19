import projectile as prj
import matplotlib.pyplot as plt

p1 = prj.Projectile(v0=30, x0=0, y0=0, theta=45, ro_zrak=1.22, Cd=1, masa=1, povrsina=0.01, dt=0.1)
p01 = prj.Projectile(v0=30, x0=0, y0=0, theta=45, ro_zrak=1.22, Cd=1, masa=1, povrsina=0.01, dt=0.01)
p001 = prj.Projectile(v0=30, x0=0, y0=0, theta=45, ro_zrak=1.22, Cd=1, masa=1, povrsina=0.01, dt=0.001)
p2 = prj.Projectile(v0=30, x0=0, y0=0, theta=45, ro_zrak=1.22, Cd=1, masa=1, povrsina=0.01, dt=0.01)

x_euler, y_euler = p1.range_Euler()
x01_euler, y01_euler = p01.range_Euler()
x001_euler, y001_euler = p001.range_Euler()
x_runge_kutta, y_runge_kutta = p2.range_runge_kutta()

plt.plot(x_euler, y_euler, label="Euler dt=0.1")
plt.plot(x01_euler, y01_euler, label="Euler dt=0.01")
plt.plot(x001_euler, y001_euler, label="Euler dt=0.001")
plt.plot(x_runge_kutta, y_runge_kutta, c="r", label="Runge-Kutta dt=0.01")

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Usporedba putanja kosog hica\nEuler i Runge-Kutta")
plt.legend()
plt.show()