import math, numpy, pylab

def pi_quant(beta, x):
    return math.sqrt(math.tanh(beta / 2.0) / math.pi) * math.exp( - x*x * math.tanh(beta/2.))

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

# Harmonic density matrix in the Trotter approximation (returns the full matrix)
def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])

x_max = 5.0                              # the x range is [-x_max,+x_max]
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-5)                   # initial value of beta (power of 2)
#beta     = 2.0 ** 4                      # actual value of beta (power of 2)
beta     = 2.0 ** 2   
rho = rho_harmonic_trotter(x, beta_tmp)  # density matrix at initial beta
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
    print 'beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp)
    
Z = sum(rho[j, j] for j in range(nx + 1)) * dx
pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
f = open('data_harm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
x1 = []
y1 = []
for j in range(nx + 1):
    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
    x1.append(x[j])
    y1.append(rho[j, j] / Z)
f.close()

vfun_quant = numpy.vectorize(pi_quant)
y_quant =  vfun_quant(beta, x)

pylab.plot(x, y1, "r-", label='simulation', linewidth=2)
pylab.plot(x, y_quant, "b--", label='quantum mechanical', linewidth=2)
pylab.xlabel('x')
pylab.ylabel('pi^2')
pylab.legend()
pylab.title('harmonic potential matrix squaring at finite temperature\nbeta = {:-f}'.format(beta))
pylab.grid()
pylab.savefig('psi_2_2.png')
pylab.show()

