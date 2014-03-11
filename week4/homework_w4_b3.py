import math, random, pandas
 
def Vol1_cyl(dimension):
    return (math.pi ** ((dimension - 1) / 2.0)) / math.gamma((dimension - 1) / 2.0 + 1.0)
   
def Vol1_cyl_markov_est(dimensions, trials):
    position = [0.0] * (dimensions - 1)
    position.append(0.0)
    n_hits = 0
    for i in range(trials):
        k = random.randint(0, dimensions - 1)
        if(k == dimensions - 1):
            x_supp = random.uniform(-1.0, 1.0)
            position[-1] = x_supp
        else:
            d_new_k = position[k] + random.uniform(-1.0, 1.0)
            if abs(d_new_k) < 1.0:
                position[k] = d_new_k
        if sum(p ** 2 for p in position[:-1]) < 1.0:
            n_hits += 1
    return n_hits / (2 * float(trials)) * 2 ** dimensions, n_hits
   
result = []
trials = 1000000
d = 0
 
print '%i used for all' % trials
while True:
    d += 1
    vol_est, n_hits = Vol1_cyl_markov_est(d, trials)
    result.append({ 'd':                         d,
                    'estimation of Vol1_cyl(d)': vol_est,
                   'Vol1_cyl(d) (exact)':       Vol1_cyl(d),
                    'n_hits':                    n_hits })
    if d == 3:
        break
 
ordered_cols = ['d', 'estimation of Vol1_cyl(d)', 'Vol1_cyl(d) (exact)', 'n_hits']
result_frame = pandas.DataFrame(result, columns=ordered_cols)
print result_frame.to_string(index=False)