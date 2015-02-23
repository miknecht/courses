
import cmath, math

def psifunc(N, delta):
    psi = complex(0,0)
    for i in range(N):
        psi = psi + cmath.exp(N * complex(0,1) * (i / N + delta))
    return psi / float(N)



N = 6

    
print psifunc(N, 0)
print psifunc(N, 2. * math.pi / N / 2)
print psifunc(N, 2. * math.pi / 360 * 15)
print psifunc(N, 0) + psifunc(N, 2. * math.pi / N / 2)    




