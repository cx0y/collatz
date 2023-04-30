import matplotlib.pyplot as plt

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
lim = eval(input("Enter Lim:"))
seeds = [i+1 for i in range(lim)]
gen = seqgen(seeds)
print(gen)
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
    plt.scatter(xmax, ymax)
    plt.grid(color="#000088")
    #plt.plot(i[0], i[1])
    #plt.scatter(i[0], i[1], s=20
    #plt.scatter(i[0], i[1], color= '#000000', s=20, edgecolors='#00FFFF')
plt.show()
