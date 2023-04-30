#cx0y ()
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def collatz(seed):
    i = 0
    seq = []
    x = []
    seq.append(seed)
    x.append(0)
    while seed > 1:
        if (seed % 2):
            seed = 3*seed + 1
        else:
            seed = seed//2
        i += 1
        seq.append(seed)
        x.append(i)
    return [x, seq]

def seqgen(list):
    x = []
    for i in list:
        seq = collatz(i)
        x.insert(i, seq)
    return x

seeds = []
#inputs = [i for i in input("Seeds: ").split()]
seeds = [int(item) for item in input("Seeds: ").split()]
#seeds = [n for n in inputs if n.isdigit()]
#print(inputs, seeds)
gen = seqgen(seeds)

if len(seeds) == 1:
    fig, ax = plt.subplots()
    ax.set_facecolor((0, 0, 0))
    fig.set_facecolor((0, 0, 0))
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    plt.title("Collatz Visualization", color="#fff")
    plt.xlabel("Stoping Time", color="#fff")
    plt.ylabel("Seed", color="#fff")
    plt.get_current_fig_manager().full_screen_toggle()
    x = []
    y = []
    def xplot(i):
        x.append(gen[0][0][i])
        y.append(gen[0][1][i])
        ax.clear()
        ax.yaxis.grid(color="#808080")
        for i, j in zip(x, y):
            if (j == max(gen[0][1]) or j == min(gen[0][1])):
                ax.text(i, j+1, '({}, {})'.format(i, j), color="#fff")
                ax.scatter(i, j, color= '#000000', s=20, edgecolors='#00FFFF')
        ax.plot(x, y, '#00FFFF', lw=1)
    ani = FuncAnimation(fig, xplot, frames=2000000, interval=100, repeat=False)
    print("seed:",gen[0][1][0],"st:",len(gen[0][0]), gen[0])
    
else:
    plt.figure(facecolor='black')
    plt.axes().spines['bottom'].set_color('white')
    plt.axes().spines['left'].set_color('white')
    plt.axes().set_facecolor("black")
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')
    plt.get_current_fig_manager().full_screen_toggle()
    for i in gen:
        print("seed:",i[1][0],"st:",len(i[0]), i)
        plt.title("Collatz Visualization", color="#fff")
        plt.xlabel("Stoping Time", color="#fff")
        plt.ylabel("Seed", color="#fff")
        ymax = max(i[1])
        xmax = i[0][i[1].index(ymax)]
        #ymin = i[1][len(i[1])]
        #xmin = i[0][len(i[0])]
        plt.text(xmax, ymax+1, '({}, {}, N = {})'.format(xmax, ymax, i[1][0]), color="#fff")
        #plt.text(xmin, ymin+0.5, '({}, {})'.format(xmin, ymin), color="#fff")
        plt.grid(color="#000088")
        plt.plot(i[0], i[1])
        #plt.scatter(i[0], i[1], s=20)
        #plt.scatter(i[0], i[1], color= '#000000', s=20, edgecolors='#00FFFF')

plt.show()

