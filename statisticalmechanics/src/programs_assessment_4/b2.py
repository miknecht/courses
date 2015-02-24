import random, math

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

d = 2
x = [0] * d
delta = 0.1

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


result = 2.0 * float(n_hits) / float(n_trials)

print d, result, V_sph(d) / V_sph(d - 1), abs(result - V_sph(d) / V_sph(d - 1)) 


