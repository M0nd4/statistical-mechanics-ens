import math
 
n_states = 40
Energies = [0.5 + i for i in range(n_states)]
grid_x = [i * 0.2 for i in range(-25, 26)]
psi = {}
for x in grid_x:
    psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
    psi[x].append(math.sqrt(2.0) * x * psi[x][0])
    for n in range(2, n_states):
        psi[x].append(math.sqrt(2.0 / n) * x * psi[x][n - 1] -
                      math.sqrt((n - 1.0) / n) * psi[x][n - 2])
 
beta = 2.0
total = 0.0
for energy in Energies:
    total += math.exp(-beta * energy)
print 'a =', total
print 'b =', sum(grid_x) * 0.2
print 'c =', 1 / (2 * math.sinh(beta/2.0))
