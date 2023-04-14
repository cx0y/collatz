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

def xplot(i):
    x_l.append(pf[1][i])
    y_l.append(pf[0][i])
    ax.clear()
    ax.plot(x_l, y_l)

ani = FuncAnimation(fig, xplot, frames=2000000, interval=100, repeat=False)
plt.show()
