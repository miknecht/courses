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
print low
data_low = []
data_high = []
high = low[:]
for step in xrange(nsteps):
    k = random.choice([0, 1])
    low[k] = levy_harmonic_path(1)[0]
    high[k] = low[k]
    data_low.append(high[k])
    data_high.append(low[k])
    
    
print high

x = [ x_max * i / M for i in range(-M, M + 1)]

pylab.plot(x, [ pi_x(x, beta) for x in x], label='path')
pylab.hist(data_high, normed=True, bins=100, label='harmonic path')
pylab.hist(data_low, normed=True, bins=100, label='harmonic path')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('imaginary time')
pylab.title('naive_harmonic_path (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-x_max, x_max)
pylab.savefig('plot_path_beta%s.png' % beta)
pylab.show()
