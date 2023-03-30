import matplotlib.pyplot as plt
import numpy as np

M=[0.052,0.124,0.168,0.236,0.284,0.336]
φ= [0.1745,0.3491,0.5236,0.6981,0.8727,1.0472]


φ1=np.array(φ)

suma = 0
for i in range(len(M)):
    suma+=M[i]*φ[i]
xy = suma/len(M)
suma2= 0
for i in range(len(M)):
    suma2 += φ[i]**2
x2 = suma2/len(M)
y2=suma/len(φ)
a = xy/x2
M1 = a*φ1

plt.plot(φ,M1,color="red")
plt.xlabel("φ[rad]")
plt.ylabel("M[N/m]")
plt.scatter(φ,M,color="blue")
plt.show()