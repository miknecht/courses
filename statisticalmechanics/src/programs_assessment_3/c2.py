import os, random, pylab, math, cmath

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
                cir = pylab.Circle((((x % 1.0) + ix) , ((y % 1.0) + iy) ), radius=sigma,  fc='r')
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
    b = [(a[0] + random.uniform(-delta, delta)) % 1.0, (a[1] + random.uniform(-delta, delta))% 1.0]
    min_dist = min(dist(b, c) for c in L if c != a)
    if not (min_dist < 4.0 * sigma_sq):
        a[:] = b
    return L

def gen(k):
    delxy = 0.5 / k
    two_delxy = 2 * delxy
    return [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(k) for j in range(k)]


def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)


def format(value):
    return "%.4f" % value

k = 8
N = k*k

eta_max = math.pi / 4
eta_b4 = 0.42
eta_b5 = 0.72
eta = eta_b5

title = 'Markov disk with periodic boundary condition\nN = %i, eta = %.2f' % (N, eta)

basefilename = 'N%i_eta%.2f.txt' % (N, eta)
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
    L = gen(k)
    print 'starting from a generated configuration'
 

print 'eta = ', eta
print 'N = ', N, len(L)
sigma = math.sqrt(eta / N / math.pi)

print 'sigma = ', sigma
#n_runs = 10
n_runs = 1000000


f2 = open('psi.dat', 'w')
for run in range(n_runs):
    if(run % 100 == 0):
        psi = Psi_6(L, sigma)
        f2.write(eta + ' ' + str(psi.real) +  ' ' + str(psi.imag) + '\n')
    if(run % 10000 == 0 and eta > 0.2):
        eta = eta - 0.02
        sigma = math.sqrt(eta / float(N) / math.pi)
        print 'eta =', eta
    L = markov_disks(L, sigma)
f2.close()

print 'Psi_6 = ', Psi_6(L, sigma)
#print L
show_conf(L, sigma, title, basefilename + '.png')

# print 'writing to file', filename
# f = open(filename, 'w')
# for a in L:
#    f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
# f.close()

