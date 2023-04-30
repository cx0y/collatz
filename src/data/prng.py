def seed(seed):
    prngs = []
    prngs.append(seed)
    while seed > 1:
        if (seed % 2):
            seed = 3*seed + 1
        else:
            seed = seed // 2
        prngs.append(seed)
    return prngs

def lim(seed, ll, ul):
    x = []
    for i in seed:
        if (i < ul) & (i > ll):
            x.append(i)
    return x

#random = lim(seed(989345275647), 1, 100)
random = seed(989345275647)
print(random)

