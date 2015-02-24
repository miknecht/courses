import random

x, y, z = 0.0, 0.0, 0.0
delta = 0.1
n_trials = 50000000
n_hits = 0
for _ in range(n_trials):
    del_x, del_y, del_z = random.uniform(-delta, delta), random.uniform(-delta, delta), random.uniform(-delta, delta)
    dx, dy, dz = x + del_x, y + del_y, z + del_z
    if(dx ** 2 + dy ** 2 + dz ** 2 < 1.0):
        x, y, z, alpha = dx, dy, dz, random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 + z ** 2 + alpha ** 2 < 1.0: n_hits += 1

print 2.0 * float(n_hits) / float(n_trials)

