import matplotlib.pyplot as plt
import numpy as np

A = np.arange(5,35,0.1)               # atten/bounce
b = [2.0,4.0,5.0]             # bounces in 1,2,3


plt.figure(1)
for i,x in enumerate(b):
    T = x*A
    plt.plot(A,T,'b')

xl = [A[0],A[-1]]
yl = [60.0,60.0]
plt.plot(xl,yl,'--')

plt.xlabel('Attenuation/reflection [dB]')
plt.ylabel('Attenuation [dB]')
plt.axis([5,31,0,80])
plt.grid()
plt.text(18.2,32,'1',fontsize=14)
plt.text(13.0,49,'2',fontsize=14)
plt.text(9,47,'3',fontsize=14)
