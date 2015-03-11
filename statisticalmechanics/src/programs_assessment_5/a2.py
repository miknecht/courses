import random, math, pylab, numpy

def psi_n_square(x, n):
    if n == -1:
        return 0.0
    else:
        psi = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
        psi.append(math.sqrt(2.0) * x * psi[0])
        for k in range(2, n + 1):
            psi.append(math.sqrt(2.0 / k) * x * psi[k - 1] -
                       math.sqrt((k - 1.0) / k) * psi[k - 2])
        return psi[n] ** 2

#beta = 0.2
beta = 1
#beta = 5


def pi_quant(x):
    return math.sqrt(math.tanh(beta / 2.0) / math.pi) * math.exp( - x*x * math.tanh(beta/2.))

def pi_class(x):
    return math.sqrt(beta / (2.0 * math.pi)) *  math.exp(- beta * x * x / 2)

def E_n(n):
    return n + 1/2

def p(n,m,x):
    return min(1, (psi_n_square(x, m) / psi_n_square(x, n)) * math.exp(-beta*(E_n(m)-E_n(n))))


histo_data = []

n = 0
x = 0.0
delta = 0.5
for k in xrange(10000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  psi_n_square(x_new, n) / psi_n_square(x, n): 
        x = x_new 
    m = n + random.choice([-1,1])
#    print n,m
    if m >= 0 and random.uniform(0.0, 1.0) < p(m, n, x):
        n = m 
    print x
    histo_data.append(x)
        
t = numpy.arange(-4, 4, 0.1)
vfun_quant = numpy.vectorize(pi_quant)
y_quant =  vfun_quant(t)

vfun_class = numpy.vectorize(pi_class)
y_class =  vfun_class(t)

pylab.hist(histo_data, bins=100, normed=True)
pylab.plot(t, y_quant, "r-")
pylab.plot(t, y_class, "b-")
pylab.xlabel('x')
pylab.ylabel('Psi_n^2')
pylab.title('Particle in a harmonic potential')
pylab.grid()
pylab.savefig('psi_2_2.png')
pylab.show()


