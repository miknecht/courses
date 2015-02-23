import random, math, pylab

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  d_x**2 + d_y**2


def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle(((x + ix) , (y + iy) ), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()

def markov_disks(L, sigma):
    sigma_sq = sigma ** 2
    delta = 0.1
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b,c) for c in L if c != a)
    if not (min_dist < 4.0 * sigma_sq):
        a[:] = b
    return L

pos = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
N = len(pos)
sigma = 0.2197

n_runs = 10000
for run in range(n_runs):
    pos = markov_disks(pos, sigma)
    
print pos
show_conf(pos, sigma, 'Markov disk with periodic boundary condition', 'test.png')
