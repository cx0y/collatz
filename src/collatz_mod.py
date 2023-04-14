# collatz mod
# rs (https://github.com/cx0y)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
time = []
x_l = []
y_l = []

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
pf = collatz(x, time, n)

fig, ax = plt.subplots()
ax.set_facecolor((0, 0, 0))
fig.set_facecolor((0, 0, 0))
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
def xplot(i):
    x_l.append(pf[1][i])
    y_l.append(pf[0][i])
    ax.clear()
    ax.plot(x_l, y_l, '#00FFFF', lw=1)
    ax.scatter(x_l, y_l, color= '#000000', s=20, edgecolors='#00FFFF')
ani = FuncAnimation(fig, xplot, frames=2000000, interval=100, repeat=False)
plt.show()
print("seed = ", pf[0], "\n stoping time = ", (len(pf[0])-1))
