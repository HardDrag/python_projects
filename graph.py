import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

arry = np.array([12.835, 11.335, 9.834, 8.334, 6.834, 5.334])
arrx = np.array([1.22, 2.72, 4.22, 5.72, 7.22, 8.72])

arry2 = np.array([9.809, 8.309, 6.809, 5.309, 3.809, 2.309])
arrx2 = np.array([1.21, 2.71, 4.21, 5.71, 7.21, 8.71])

arry3 = np.array([8.029, 6.529, 5.029, 3.529, 2.029, 0.529])
arrx3 = np.array([1.24, 2.74, 4.24, 5.74, 7.24, 8.74])

plt.figure()
plt.yscale('log')

ax = plt.gca()
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:.1f}'))
ax.yaxis.set_minor_formatter(NullFormatter())

plt.grid(True)
plt.yticks(np.arange(min(arry3), max(arry3)+2.0, 1.0))


plt.title('Stopa błędów transmisji w funkcji SNR, Bt = 300 bps')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.plot(arrx3, arry3)
plt.show()