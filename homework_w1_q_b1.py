import random, math, pylab, numpy

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    in_sq = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            in_sq += 1
        if x**2 + y**2 < 1.0: 
            n_hits += 1
    return n_hits, in_sq

def pi_values(delta):
    n_runs = 500
    n_trials = 1000
    sum = 0
    sum_in_sq = 0
    for run in range(n_runs):
        s, sis = markov_pi(n_trials, delta)
        sum += s
        sum_in_sq += sis
    return sum_in_sq / (float(n_trials * n_runs))

deltas  = [x*0.1 for x in range(1, 51)]  # range  0.1, 0.2, 0.3 ... 5.0
accepts = [pi_values(d) for d in deltas]

pylab.plot(deltas, accepts, 'o')
pylab.xlabel('deltas')
pylab.ylabel('acceptance ratios')
pylab.savefig('acceptance ratios with varying deltas.png')
pylab.show()
