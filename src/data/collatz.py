# Collatz Conjecture
import matplotlib.pyplot as plt

MAX = eval(input("Max: "))
n_list = range(1,MAX+1)
steps = list()

for n in n_list:
    count = 0
    while not n == 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    steps.append(count)

plt.xlabel("$n$",fontsize=18)
plt.ylabel("Steps to reach 1")
plt.title("Collatz Conjecture")
plt.plot(n_list,steps,'o',color="blue", ms=.5, mec="red",mew=0.0)
plt.xlim(xmax=MAX)
plt.ylim(ymin=0)
plt.savefig("collatz_"+str(MAX)+".png",bbox_inches="tight",dpi=600)
plt.show()
