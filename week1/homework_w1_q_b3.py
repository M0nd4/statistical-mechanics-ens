import random, math, pylab, numpy

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0: n_hits += 1
    return n_hits

def pi_values(delta):
    n_runs = 1000
    n_trials = 4000
    sum = 0.0
    sigma = 0.0
    for run in range(n_runs):
        pi_est = 4.0 * markov_pi(n_trials, delta) / float(n_trials)
        sum += pi_est
        sigma += (pi_est - math.pi) ** 2
    return sum / float(n_runs), math.sqrt(sigma/(n_runs))

#deltas  = [x*0.1 for x in range(9, 16)]  # range  0.9, 1.0, 1.1 ... 2.0
deltas  = [x*0.1 for x in range(1, 51)]  # range  0.1, 0.2, 0.3 ... 5.0
accepts = [pi_values(d) for d in deltas]
rmses   = [a[1] for a in accepts]

print 'Data'
print deltas
print rmses

pylab.plot(deltas, rmses, 'o')
pylab.xlabel('delta')
pylab.ylabel('rms error')
pylab.savefig('rms error varying deltas b3.png')
pylab.show()
