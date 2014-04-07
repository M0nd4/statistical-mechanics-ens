import random, math, pylab

L = 16
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
nsteps = 10
T = 3.0
beta = 1.0 / T
S0 = [1] * N
S1 = [-1] * N
k = {}
Upsilon = {}
n_diff = 10
xs = []
ys = []
while n_diff != 0:
    nsteps *= 2
    for step in range(-nsteps, 0):
        if step not in k:
            k[step] = random.randint(0, N - 1)
            Upsilon[step] = random.uniform(0.0, 1.0)
        h = sum(S0[nn] for nn in nbr[k[step]])
        S0[k[step]] = -1
        if Upsilon[step] < 1.0 / (1.0 + math.exp(-2.0 * beta * h)):
            S0[k[step]] = 1
        h = sum(S1[nn] for nn in nbr[k[step]])
        S1[k[step]] = -1
        if Upsilon[step] < 1.0 / (1.0 + math.exp(-2.0 * beta * h)):
            S1[k[step]] = 1
    n_diff = 0
    for i in range(N):
        if S0[i] != S1[i]: n_diff += 1
    print nsteps, n_diff
    xs.append(nsteps)
    ys.append(n_diff)

pylab.title("Differences between systems' configuartions vs time")
pylab.plot(xs, ys, 'o-', linewidth=2.0)
# pylab.xlim(0.0, 5.5)
# pylab.ylim(0.0, max(sweeps) * 1.1)
pylab.xlabel('Steps')
pylab.ylabel('Differences between systems')
pylab.savefig('system_diffs_vs_time.png')
pylab.show()
