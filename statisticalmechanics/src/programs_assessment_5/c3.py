import math, numpy, pylab

def pi_quant(beta, x):
    return math.sqrt(math.tanh(beta / 2.0) / math.pi) * math.exp( - x*x * math.tanh(beta/2.))

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def V(x, cubic, quartic): 
    return x * x / 2.0 + cubic * x * x * x + quartic * x * x * x * x

def Energy_pert(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z_pert(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy_pert(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

def Z(cubic, quartic, beta, nx):
    x_max = 5.0                              # the x range is [-x_max,+x_max]    
    dx = 2.0 * x_max / (nx - 1)
    x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
    beta_tmp = 2.0 ** (-5)                   # initial value of beta (power of 2)
    rho = rho_anharmonic_trotter(x, beta_tmp, quartic, cubic)  # density matrix at initial beta
    while beta_tmp < beta:
        rho = numpy.dot(rho, rho)
        rho *= dx
        beta_tmp *= 2.0
    return sum(rho[j, j] for j in range(nx + 1)) * dx


def rho_anharmonic_trotter(grid, beta, quartic, cubic):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * \
                         (V(x, cubic, quartic) + V(xp, cubic, quartic))) \
                         for x in grid] for xp in grid])


beta     = 2.0 ** 2 
nx = 100
a = [0.001,0.01, 0.1, 0.2,0.3, 0.4, 0.41]

for aa in a:
    quartic =  aa
    cubic = -aa
    z1 = Z(cubic, quartic, beta, nx)
    z2 = Z_pert(cubic, quartic, beta, nx)
    print aa, z1, z2, abs(z1-z2)

