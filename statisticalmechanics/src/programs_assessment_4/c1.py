import random, math, pylab

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

def V_sph_2(dim, q):
    prod = 2
    if(dim==1):
        return prod
    for i in range(0, dim -1):
        prod *= q[i]
    return prod
    

def Q(dim):
    d = dim - 1
    x = [0] * d
    delta = 0.1
    n_trials = 100000
    n_hits = 0
    old_radius_square = 0
    for _ in range(n_trials):
        k = random.randint(0, d - 1)
        x_old_k = x[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
        if(new_radius_square < 1.0):
            old_radius_square = new_radius_square
            x[k], alpha = x_new_k, random.uniform(-1.0, 1.0)
        if old_radius_square + alpha ** 2 < 1.0: n_hits += 1
    return 2.0 * float(n_hits) / float(n_trials) 


d_max = 200
q = []
for d in range(2, d_max + 1):
    q.append(Q(d))


#print 4, 2 * q[0] * q[1] * q[2], V_sph_2(4, q), math.pi * math.pi / 2.0

x = []
y = []
z = []
for d in range(1, d_max):
    x.append(d)
    y.append(V_sph_2(d, q))
    z.append(V_sph(d))


pylab.title("volume up to dim = 200")
pylab.xlabel('dimension')
pylab.ylabel('volume')
pylab.yscale('log')
pylab.plot(x, y, "r")
pylab.plot(x, z, "b")
pylab.show()
pylab.savefig("v.png")
pylab.close()


