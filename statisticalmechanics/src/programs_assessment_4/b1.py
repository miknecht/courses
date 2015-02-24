import random, pylab, math, numpy

def f_4(r):
    return 4 * r**3

def f_N(r, N):
    return float(N) * r**(N-1)

d = 20
x = [0] * d
delta = 0.1

histo_data = []

n_trials = 5000000
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
    histo_data.append(math.sqrt(old_radius_square))


t = numpy.arange(0., 1., 0.02)

print 2.0 * float(n_hits) / float(n_trials)
pylab.hist(histo_data, bins=100, normed=True)
pylab.plot(t, f_N(t), "ro")
pylab.xlabel('r')
pylab.ylabel('frequency')
pylab.title('P(r) and Q for d = 4')
pylab.grid()
pylab.savefig('q_n.png')
pylab.show()
