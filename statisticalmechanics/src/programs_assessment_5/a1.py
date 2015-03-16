import random, math, pylab, numpy


def psi_0(x):
    return (1.0 / (math.pi)**(1./4.)) * math.exp(- x*x / 2.0)

def psi_2_squard(x):
    t = psi_0(x)
    return t*t

histo_data = []

x = 0.0
delta = 0.5
for k in xrange(1000000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  psi_2_squard(x_new) / psi_2_squard(x): 
        x = x_new 
    histo_data.append(x)
    
t = numpy.arange(-4, 4, 0.1)
vfun = numpy.vectorize(psi_2_squard)
y =  vfun(t)

pylab.hist(histo_data, bins=100, normed=True, label='QMC')
pylab.plot(t, y, "r-", label='Quantum mechanical')
pylab.xlabel('x')
pylab.ylabel('Psi_0^2')
pylab.legend()
pylab.title('Particle in a harmonic potential')
pylab.grid()
pylab.savefig('psi_2_2.png')
pylab.show()


