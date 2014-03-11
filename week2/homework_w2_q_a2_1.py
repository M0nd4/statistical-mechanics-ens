import random, pylab
 
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.05
n_steps = 10000000
histo_data = []
 
for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta),
         a[1] + random.uniform(-delta, delta)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist < 4.0 * sigma_sq):
        a[:] = b
    histo_data.append(a[:][0])
   
pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x position (bucketed)')
pylab.ylabel('frequency')
pylab.title('Markov Chain distribution of disk position vs frequency. Question A2.1')
pylab.grid()
pylab.savefig('markov_disks_histo_%.3f.png' % delta)
pylab.show()
