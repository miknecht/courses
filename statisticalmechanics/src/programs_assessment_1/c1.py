import random, math

n_trials = 400000
n_hits = 0
var = 0.0
var2 = 0.0
for i in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
    var += (Obs - math.pi)**2
    var2 += Obs * Obs

a = math.sqrt(var / float(n_trials))
b = var2 / float(n_trials)

print 4.0 * n_hits / float(n_trials), a, b, math.sqrt(b - a*a) 


