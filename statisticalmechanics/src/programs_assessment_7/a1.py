import math, random, pylab

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def pi_x(x, beta):
    sigma = 1.0 / math.sqrt(2.0 * math.tanh(beta / 2.0))
    return math.exp(-x ** 2 / (2.0 * sigma ** 2)) / math.sqrt(2.0 * math.pi) / sigma

x_max = 5.
M = 100
N = 2
beta = 2.0
nsteps = 1000000
low = levy_harmonic_path(2)
data = []
high = low[:]
for step in xrange(nsteps):
    k = random.choice([0, 1])
    low[k] = levy_harmonic_path(1)[0]
    high[k] = low[k]
    data.append(high[k])
    

x = [ x_max * i / M for i in range(-M, M + 1)]

pylab.plot(x, [ pi_x(x, beta) for x in x], label='$\pi_{calc}(x,beta)$')
pylab.hist(data, normed=True, bins=100, label='$\pi_{sample}(x,beta)$')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\pi$')
pylab.title('levy harmonic path (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-x_max, x_max)
pylab.savefig('plot_levy_harmonic_path%s.png' % beta)
pylab.show()
