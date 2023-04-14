import matplotlib.pyplot as plt

data = []
base = []

def collatz(collatz, n):
    while n > 1:
        if (n % 2):
            n = 3*n + 1
        else:
            n = n//2
        collatz.append(n)
    return collatz


n = int(input('Enter Range: '))
for i in range(n):
    x = []
    qt = collatz(x, i)
    if (1 in qt):
        data.append(-1)
    else:
        data.append(1)
    base.append(i)

plt.figure(facecolor='black')
plt.axes().spines['bottom'].set_color('white')
plt.axes().spines['left'].set_color('white')
plt.axes().set_facecolor("black")
plt.tick_params(axis='x', colors='white')
plt.tick_params(axis='y', colors='white')
plt.plot(base, data, '#00FFFF', linewidth=1)

plt.show()
