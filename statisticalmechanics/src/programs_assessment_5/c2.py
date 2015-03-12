import math, random, pylab, numpy

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta)) 

def pi_quant(beta, x):
    return math.sqrt(math.tanh(beta / 2.0) / math.pi) * math.exp( - x*x * math.tanh(beta/2.))

def V(x, cubic, quartic): 
    return 0.5 * x * x + cubic * x * x * x + quartic * x * x * x * x


def read_file(filename):
    list_x = []
    list_y = []
    with open(filename) as f:
        for line in f:
            x, y = line.split()
            list_x.append(float(x))
            list_y.append(float(y))
    f.close()
    return list_x, list_y

quartic = 1
cubic = -1  

histo_data = []
beta = 4.0
N = 8                                             # number of slices
dtau = beta / N
delta = 1.0                                       # maximum displacement on one slice
n_steps = 4000000                                 # number of Monte Carlo steps
x = [0.0] * N                                     # initial path
for step in range(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-dtau * V(x[k], cubic, quartic)))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-dtau * V(x_new, cubic, quartic)))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    histo_data.append(x[0])

t = numpy.arange(-10, 10, 0.1)
vfun_quant = numpy.vectorize(pi_quant)
y_quant =  vfun_quant(beta, t)

filename = 'data_anharmonic_matrixsquaring_beta' + str(beta) + '.dat'
list_x, list_y = read_file(filename)

pylab.hist(histo_data, bins=100, normed=True)
pylab.plot(list_x, list_y, "r-")
#pylab.plot(t, y_quant, "b-")
pylab.xlabel('x')
pylab.ylabel('pi_n^2 (sim blue, quant blue)')
pylab.title('Path-integral MC algo. for the unharmonic oscillator\ntemperature\nbeta = {:-f} quartic = {:-f}, cubic = {:-f}'.format(beta, quartic, cubic))
pylab.grid()
pylab.savefig('psi_2_2.png')
pylab.show()
