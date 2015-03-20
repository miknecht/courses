import math, random, pylab

def V(x, cubic, quartic):
    pot = x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot


def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x


def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + 1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x


beta = 20.0
N = 80
Ncut = N / 2
dtau = beta / N
print dtau 
delta = 1.0
n_steps = 400000
cubic = -1
quartic = 1
#cubic = 0
#quartic = 0
data = []

x = [0] * N
weight_old = 0.00001
data = []
for step in range(n_steps):
    x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    s = sum(-V(a, cubic, quartic) * dtau for a in x_new)
    weight_new = math.exp(s)
    if random.uniform(0.0, 1.0) <  min(1, weight_new/ weight_old) :
        weight_old = weight_new
        x = x_new[:]
    if step % 50 == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])


pylab.hist(data, normed=True, bins=100, label='QMC')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
#pylab.plot(list_x, list_y, label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.title('levy_harmonic_path (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-2, 2)
pylab.ylim(0, 10)
pylab.savefig('plot_B1_beta%s.png' % beta)
pylab.show()
