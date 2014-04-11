import random, math
 
def unit_sphere():
    x = [random.gauss(0.0, 1.0) for i in range(3)]
    norm =  math.sqrt(sum(xk ** 2 for xk in x))
    return [xk / norm for xk in x]
 
def minimum_distance(positions, N):
    dists = [math.sqrt(sum((positions[k][j] - positions[l][j]) ** 2 \
             for j in range(3))) for l in range(N) for k in range(l)]
    return min(dists)
 
def resize_disks(positions, r, N, gamma):
    Upsilon = minimum_distance(positions, N) / 2.0
    r = r + gamma * (Upsilon - r)
    return r
 
N = 13
gamma  = 0.09
min_density = 0.78
for iteration in range(100):
    print iteration
    sigma  = 0.25
    r = 0.0
    positions = [unit_sphere() for j in range(N)]
    n_acc = 0
    step = 0
    while sigma > 1.e-8:
        step += 1
        if step % 500000 == 0:
            eta = N / 2.0 * (1.0 - math.sqrt(1.0 - r ** 2))
            print r, eta, sigma, n_acc
        k = random.randint(0, N - 1)
        newpos = [positions[k][j] + random.gauss(0, sigma) for j in range(3)]
        norm = math.sqrt(sum(xk ** 2 for xk in newpos))
        newpos = [xk / norm for xk in newpos]
        new_min_dist = min([math.sqrt(sum((positions[l][j] - newpos[j]) ** 2 \
                       for j in range(3))) for l in range(k) + range(k + 1, N)])
        if new_min_dist > 2.0 * r:
            positions = positions[:k] + [newpos] + positions[k + 1:]
            n_acc += 1
        if step % 100 == 0:
            acc_rate = n_acc / float(100)
            n_acc = 0
            if acc_rate < 0.2:
                sigma *= 0.5
            elif acc_rate > 0.8 and sigma < 0.5:
                sigma *= 2.0
            r = resize_disks(positions, r, N, gamma)
            R = 1.0 / (1.0 / r - 1.0)
            eta = 1.0 * N / 2.0 * (1.0 - math.sqrt(1.0 - r ** 2))
    print 'final density: %f (gamma = %f)' % (eta, gamma)
    if eta > min_density:
        f = open('N_' + str(N) + '_final_'+ str(eta) + '.txt', 'w')
        for a in positions:
           f.write(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + '\n')
        f.close()
 
# Best output, with r = 0.476 (approx):
#0.951285048909    0.096244941837   -0.292905559683
#-0.836693954549  -0.0452742138496  -0.545796181721
#0.735620479897    0.26475747826     0.623511016151
#0.612322027089   -0.781345646303   -0.120667792495
#-0.500099723875  -0.814282852896    0.294692554469
#-0.431031661774   0.857393625433    0.281225670264
#0.275727812605   -0.0123370091164  -0.961156580148
#-0.26357267885    0.713368626483   -0.649334001661
#0.464617033369    0.883912489825   -0.0531951373283
#-0.206742372841  -0.761669991291   -0.614098050509
#0.300829747658   -0.576107932556    0.760000732217
#-0.914027960106   0.0410157071377   0.403572298248
#-0.160028165771   0.238238603857    0.957931810617
