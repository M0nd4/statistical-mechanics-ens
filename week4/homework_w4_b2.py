import math, random, pandas
 
def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0)) / math.gamma(dimension / 2.0 + 1.0)
   
def Vol1_s_markov_est(dimensions, trials):
    position = [0.0] * dimensions
    n_hits = 0
    for i in range(trials):
        k = random.randint(0, dimensions - 1)
        d_new_k = position[k] + random.uniform(-1.0, 1.0)
        if abs(d_new_k) < 1.0:
           position[k] = d_new_k
        if sum(p ** 2 for p in position) < 1.0:
            n_hits += 1
    return n_hits / float(trials) * 2 ** dimensions, n_hits
   
result = []
trials = 1000000
d = 0
 
print '%i used for all' % trials
while True:
    d += 1
    vol_est, n_hits = Vol1_s_markov_est(d, trials)
    result.append({ 'd':                       d,
                    'estimation of Vol1_s(d)': vol_est,
                    'Vol1_s(d) (exact)':       Vol1_s(d),
                    'n_hits':                  n_hits })
    if d == 3:
        break
 
ordered_cols = ['d', 'estimation of Vol1_s(d)', 'Vol1_s(d) (exact)', 'n_hits']
result_frame = pandas.DataFrame(result, columns=ordered_cols)
print result_frame.to_string(index=False)