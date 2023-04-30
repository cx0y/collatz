# plotting straght line with grediant of colatger sequence
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

m = []
time = []
x = np.linspace(0, 1000, 1000)

def collatz(collatz, time_list, n):
    i = 0
    collatz.append(n)
    time_list.append(0)
    while n > 1:
        if (n % 2):
            n = 3*n + 1
        else:
            n = n//2
        i += 1
        collatz.append(n)
        time_list.append(i)
    return [collatz, time_list]

n = int(input('Enter n: '))
pf = collatz(m, time, n)

for i in range(len(pf[0])):
    y = []
    for j in range(len(x)):
        m = pf[0][i]*np.log(x[j]) + pf[1][i]
        y.append(m)
    plt.plot(x, y)
plt.plot(pf[1],pf[0])
plt.show()

