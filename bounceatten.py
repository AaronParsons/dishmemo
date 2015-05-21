import matplotlib.pyplot as plt
import numpy as np

A = np.arange(5,21,0.1)               # atten/bounce
b = [1.0,3.0,5.0]             # bounces in 1,2,3


plt.figure(1)
for i,x in enumerate(b):
    T = x*A
    plt.plot(A,T,'b')

xl = [A[0],A[-1]]
yl = [60.0,60.0]
plt.plot(xl,yl,'--')

plt.xlabel('Attenuation/bounce [dB]')
plt.ylabel('Attenuation [dB]')
plt.axis([5,21,0,80])
plt.grid()
plt.text(18.2,15,'1',fontsize=14)
plt.text(15.0,41,'2',fontsize=14)
plt.text(9,42,'3',fontsize=14)
