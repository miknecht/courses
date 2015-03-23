import math, random, pylab
from _dbus_bindings import Double

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def rho_harm_1d(x, xp, beta):
    Upsilon_1 = (x + xp) ** 2 / 4.0 * math.tanh(beta / 2.0)
    Upsilon_2 = (x - xp) ** 2 / 4.0 / math.tanh(beta / 2.0)
    return math.exp(- Upsilon_1 - Upsilon_2)

def z(beta):
    return 1.0 / (1.0 - math.exp(- beta))

def pi_two_bosons(x, beta):
    pi_x_1 = math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta / 2.0))
    pi_x_2 = math.sqrt(math.tanh(beta)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta))
    weight_1 = z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta))
    weight_2 = z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta))
    pi_x = pi_x_1 * weight_1 + pi_x_2 * weight_2
    return pi_x

beta = 2.0
nsteps = 1000
low = levy_harmonic_path(2)
high = low[:]

def func(beta, nsteps):
    prob_one_cycle = 0
    prob_two_cycles = 0 
    for step in xrange(nsteps):
        # move 1
        if low[0] == high[0]:
            k = random.choice([0, 1])
            low[k] = levy_harmonic_path(1)[0]
            high[k] = low[k]
            prob_one_cycle += 1
        else:
            low[0], low[1] = levy_harmonic_path(2)
            high[1] = low[0]
            high[0] = low[1]
            prob_two_cycles += 1
        # move 2
        weight_old = (rho_harm_1d(low[0], high[0], beta) *
                      rho_harm_1d(low[1], high[1], beta))
        weight_new = (rho_harm_1d(low[0], high[1], beta) *
                      rho_harm_1d(low[1], high[0], beta))
        if random.uniform(0.0, 1.0) < weight_new / weight_old:
            high[0], high[1] = high[1], high[0]            
    return 1.0 * prob_one_cycle / nsteps, 1.0 * prob_two_cycles / nsteps 
        

list_beta = [0.1 * i for i in range(1, 50)]
print list_beta

prob_one_cycle = []
prob_two_cycles = []

for beta in list_beta:
    print beta
    one_cycle, two_cycles = func(beta, nsteps)
    prob_one_cycle.append(one_cycle)
    prob_two_cycles.append(two_cycles)
    
fract_two_cycles = [z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]
fract_one_cycle = [z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]

pylab.title("$\pi$ with two bosons")
pylab.plot(list_beta, fract_two_cycles, label='$z^2(\\beta) / (z^2(\\beta) + z(2 \\beta))$')
pylab.plot(list_beta, fract_one_cycle, label='$z^2(2 \\beta) / (z^2(\\beta) + z(2 \\beta))$')
pylab.plot(list_beta, prob_two_cycles, label='prob two cycles')
pylab.plot(list_beta, prob_one_cycle, label='prob one cycle')
pylab.legend()
pylab.xlabel('$\\beta$')
pylab.ylabel('Distribution for one and two cycles')
pylab.xlim(0.2, 5)
pylab.savefig('plot_dist%s.png' % beta)
pylab.show()

        
