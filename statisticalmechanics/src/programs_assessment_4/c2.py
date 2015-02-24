import random, math

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

def V_sph_2(dim, q):
    prod = 2
    if(dim == 1):
        return prod
    for i in range(0, dim - 1):
        prod *= q[i]
    return prod
    

def Q(dim, n_trials):
    d = dim - 1
    x = [0] * d
    delta = 0.1
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


n_trials = [1, 10, 100, 1000, 10000, 100000, 1000000]

d_max = 20
n_runs = 10

for n in n_trials: 
    q_20 = 0   
    q_20_2 = 0  
    for m in range(n_runs): 
        q = []              
        for d in range(2, d_max + 1):
            q.append(Q(d, n))
        v = V_sph_2(d_max, q)
        q_20 += v
        q_20_2 += v * v
    vol = q_20 / n_runs
    err = math.sqrt(q_20_2 / n_runs - vol * vol) / math.sqrt(n_runs)
    print n, v, V_sph(d_max), err, abs(vol - V_sph(d_max))






