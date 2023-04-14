import matplotlib.pyplot as plt
y = []
x = []
inp = eval(input("Mode: S 0, L 1: "))
if(inp == 0):
    for i in range(10):
        y.append(-1)
        x.append(i+1)
    y.append(1)
    x.append(11)
    for i in range(10):
        y.append(-1)
        x.append(i+12)
else:
    for i in range(5000):
        y.append(-1)
        x.append(i+1)
    y.append(1)
    x.append(5001)
    for i in range(5000):
        y.append(-1)
        x.append(i+5002)

plt.plot(x, y)
plt.show()
