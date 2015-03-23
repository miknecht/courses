import random, math, numpy, sys, os, pylab

def levy_harmonic_path_3d(k):
    x0 = tuple([random.gauss(0.0, 1.0 / math.sqrt(2.0 *
                math.tanh(k * beta / 2.0))) for d in range(3)])
    x = [x0]
    for j in range(1, k):
        Upsilon_1 = 1.0 / math.tanh(beta) + 1.0 / \
                          math.tanh((k - j) * beta)
        Upsilon_2 = [x[j - 1][d] / math.sinh(beta) + x[0][d] /
                     math.sinh((k - j) * beta) for d in range(3)]
        x_mean = [Upsilon_2[d] / Upsilon_1 for d in range(3)]
        sigma = 1.0 / math.sqrt(Upsilon_1)
        dummy = [random.gauss(x_mean[d], sigma) for d in range(3)]
        x.append(tuple(dummy))
    return x

def rho_harm_3d(x, xp):
    Upsilon_1 = sum((x[d] + xp[d]) ** 2 / 4.0 *
                    math.tanh(beta / 2.0) for d in range(3))
    Upsilon_2 = sum((x[d] - xp[d]) ** 2 / 4.0 /
                    math.tanh(beta / 2.0) for d in range(3))
    return math.exp(- Upsilon_1 - Upsilon_2)

data_1 = []
data_2 = []
N = 64
T_star = 0.8
beta = 1.0 / (T_star * N ** (1.0 / 3.0))
# Initial condition
positions = {}
for k in range(N):
    a = levy_harmonic_path_3d(1)
    positions[a[0]] = a[0]
# Monte Carlo loop
nsteps = 2000000
for step in range(nsteps):
    # move 1: resample one permutation cycle
    boson_a = random.choice(positions.keys())
    perm_cycle = []
    while True:
        perm_cycle.append(boson_a)
        boson_b = positions.pop(boson_a)
        if boson_b == perm_cycle[0]:
            break
        else:
            boson_a = boson_b
    k = len(perm_cycle)

    data_1.append(boson_a[0])
    if(len(perm_cycle) > 10):
        data_2.append(boson_a[0])    
    
    
    perm_cycle = levy_harmonic_path_3d(k)
    positions[perm_cycle[-1]] = perm_cycle[0]
    for k in range(len(perm_cycle) - 1):
        positions[perm_cycle[k]] = perm_cycle[k + 1]
    # move 2: exchange
    a_1 = random.choice(positions.keys())
    b_1 = positions.pop(a_1)
    a_2 = random.choice(positions.keys())
    b_2 = positions.pop(a_2)
    weight_new = rho_harm_3d(a_1, b_2) * rho_harm_3d(a_2, b_1)
    weight_old = rho_harm_3d(a_1, b_1) * rho_harm_3d(a_2, b_2)
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        positions[a_1] = b_2
        positions[a_2] = b_1
    else:
        positions[a_1] = b_1
        positions[a_2] = b_2

        
        
#for boson in positions.keys():
#    print boson, positions[boson]



def psi02(x):    
    return math.exp(-x*x)/ math.sqrt(math.pi)

x_max = 3.0
M = 300
x = [ x_max * i / M for i in range(-M, M + 1)]
    
pylab.plot(x, [ psi02(x) for x in x], label='$d^{calc}(r)$')
pylab.hist(data_2, normed=True, bins=120, label='$d^{cycle}(r)$')
pylab.hist(data_1, normed=True, bins=120, label='$d(r)$')

pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('Sample')
pylab.title('levy harmonic path (beta=%s)' % (beta))
pylab.xlim(-3, 3)
pylab.savefig('plot_levy_harmonic_path%s.png' % beta)

pylab.show()
    
