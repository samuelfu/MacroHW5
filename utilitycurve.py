import matplotlib.pyplot as plt
import numpy as np

C1 = np.arange(0.01, 1.01, 0.01)
C2_1 = np.exp(-0.5 - np.log(C1))
C2_2 = np.exp(-1 - np.log(C1))
C2_3 = np.exp(-1.5 - np.log(C1))

fig, ax = plt.subplots()
ax.plot(C1, C2_1, C1, C2_2, C1, C2_3)
plt.text(0.05, 1.5, 'U = -1.5')
plt.text(0.25, 1.6, 'U = -1')
plt.text(0.4, 1.7, 'U = -0.5')

plt.ylim(0,2)
ax.set(xlabel='C1', ylabel='C2',
       title='U = ln(C1) + ln(C2)')
ax.grid()
fig.savefig("test.png")
plt.show()
