import datetime, random, math, numpy, os, pylab
 
def levy_harmonic_path(k, beta):
    ''' Where k corresponds to positions cycle; the amount of the particles that
        will be sent to different destinations rather than sent to their intended
        destination immediately above their source point (diagonal paths) '''
    xk = tuple([random.gauss(0.0, 1.0 / math.sqrt(2.0 *
                math.tanh(k * beta / 2.0))) for d in range(3)])
    x = [xk]
    for j in range(1, k):
        Upsilon_1 = 1.0 / math.tanh(beta) + 1.0 / \
                          math.tanh((k - j) * beta)
        Upsilon_2 = [x[j - 1][d] / math.sinh(beta) + xk[d] /
                     math.sinh((k - j) * beta) for d in range(3)]
        x_mean = [Upsilon_2[d] / Upsilon_1 for d in range(3)]
        sigma = 1.0 / math.sqrt(Upsilon_1)
        dummy = [random.gauss(x_mean[d], sigma) for d in range(3)]
        x.append(tuple(dummy))
    return x
 
def rho_harm(x, xp, beta):
    ''' Gives a diagonal harmonic density matrix, exchanging 2 particles '''
    Upsilon_1 = sum((x[d] + xp[d]) ** 2 / 4.0 *
                    math.tanh(beta / 2.0) for d in range(3))
    Upsilon_2 = sum((x[d] - xp[d]) ** 2 / 4.0 /
                    math.tanh(beta / 2.0) for d in range(3))
    return math.exp(- Upsilon_1 - Upsilon_2)
 
N        = 512
T_star   = 0.6
beta     = 1.0 / (T_star * N ** (1.0 / 3.0))
nsteps   = 100000
filename = 'boson_configuration_b3.txt'
 
# positions' keys are the x, y and z coordinates
#            values are the positions when Tao==Beta (at the destination)
positions  = {}
cycle_lens = []
 
if os.path.isfile(filename):
    f = open(filename, 'r')
    for line in f:
        a = line.split()
        positions[tuple([float(a[0]), float(a[1]), float(a[2])])] = \
               tuple([float(a[3]), float(a[4]), float(a[5])])
    f.close()
    if len(positions) != N:
        exit('error input file')
    print 'starting from file', filename
else:
    # Making a default setup of N-particles all with a destination immediately
    # above the source point (so no exchanges yet)
    for k in range(N):
        a = levy_harmonic_path(1, beta)
        positions[a[0]] = a[0]
    print 'starting from scratch', filename
 
start_time = datetime.datetime.now()
end_time   = start_time + datetime.timedelta(minutes=20)
print 'Finish at:', end_time
while datetime.datetime.now() < end_time:
#for step in range(nsteps):
    # choose a random particle
    boson_a = random.choice(positions.keys())
    perm_cycle = []
    # calculate the different diagonal paths it could follow
    while True:
        perm_cycle.append(boson_a)
        boson_b = positions.pop(boson_a)
        if boson_b == perm_cycle[0]:
            break
        else:
            boson_a = boson_b
    # resample drunken walks again to the desired destinations (straight or diagonal)
    k = len(perm_cycle)
    perm_cycle = levy_harmonic_path(k, beta)
    positions[perm_cycle[-1]] = perm_cycle[0]
    for k in range(len(perm_cycle) - 1):
        positions[perm_cycle[k]] = perm_cycle[k + 1]
 
    cycle_lens.append(len(perm_cycle))
 
    # pick 2 particles to exchange their destinations
    a_1 = random.choice(positions.keys())
    b_1 = positions.pop(a_1)
    a_2 = random.choice(positions.keys())
    b_2 = positions.pop(a_2)
    weight_new = rho_harm(a_1, b_2, beta) * rho_harm(a_2, b_1, beta)
    weight_old = rho_harm(a_1, b_1, beta) * rho_harm(a_2, b_2, beta)
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        positions[a_1] = b_2
        positions[a_2] = b_1
    else:
        positions[a_1] = b_1
        positions[a_2] = b_2
 
f = open(filename, 'w')
for a in positions:
   b = positions[a]
   f.write(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + ' ' +
           str(b[0]) + ' ' + str(b[1]) + ' ' + str(b[2]) + '\n')
f.close()
 
pylab.title('$\\pi(k)$ against $k$ (k: Length of cycles), B3\n' + \
            'N=%i, T_star=%.1f' % (N, T_star))
pylab.hist(cycle_lens, normed=True, bins=100)   # max(cycle_lens)) #, label='Probability of cycle_length, k')
 
pylab.ylim(0.0, 0.01)
pylab.xlabel('$k$')
pylab.ylabel('$\\pi(k)$')
# pylab.legend()
pylab.savefig('prob_k_vs_k_for_N_%i_Tstar_%.1f_q_b3.png' % (N, T_star))
# pylab.show()
