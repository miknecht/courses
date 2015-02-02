import random

x, y = 1.0, 1.0
n_trials = 2 ** 12

deltas = [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]

print "delta | acceptance rate"
for delta in deltas:
    n_hits = 0
    n_accept = 0
    for i in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            n_accept += 1
        if x**2 + y**2 < 1.0: 
            n_hits += 1
    print delta, "|", n_accept / float(n_trials)


