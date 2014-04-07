import random, math, os
 
def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E
 
L = 6
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
T = 2.0
filename = 'local_'+ str(L) + '_' + str(T) + '.txt'
S = [random.choice([1, -1]) for k in range(N)]
nsteps = N * 1000000
beta = 1.0 / T
Energy = energy(S, N, nbr)
E = []
print  'nsteps =', nsteps
for step in range(nsteps):
    k = random.randint(0, N - 1)
    delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
    if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
        S[k] *= -1
        Energy += delta_E
    E.append(Energy)
E_mean = sum(E)/ len(E)
print sum(E) / len(E) / N, 'mean energy'
