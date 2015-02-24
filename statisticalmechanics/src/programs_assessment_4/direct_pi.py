import random

n_trials = 800000
n_hits = 0
for i in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    z = random.uniform(-1.0, 1.0)
    if x**2 + y**2 + z**2 < 1.0: 
        n_hits += 1
print 2.0 * n_hits / float(n_trials)
