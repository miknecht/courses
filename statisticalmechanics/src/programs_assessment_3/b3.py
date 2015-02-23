import os, random, pylab, math

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
                cir = pylab.Circle(((x + ix) % 1.0, (y + iy) % 1.0), radius=sigma,  fc='r')
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

def gen(k):
    delxy = 0.5 / k
    two_delxy = 2 * delxy
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(k) for j in range(k)]
    return L
    
k = 8
N = k*k
L = gen(k)
N = len(L)
eta = math.pi / 4
print 'eta = ', eta
print 'N = ', N
sigma = math.sqrt(eta / N / math.pi)

show_conf(L, sigma, 'Markov disk with periodic boundary condition', 'test.png')

filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)


if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    L = []
    for k in range(N):
        L.append([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])
    print 'starting from a new random configuration'

f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()


print sigma
n_runs = 10000
for run in range(n_runs):
    L = markov_disks(L, sigma)
    
print L
show_conf(L, sigma, 'Markov disk with periodic boundary condition', 'test.png')
