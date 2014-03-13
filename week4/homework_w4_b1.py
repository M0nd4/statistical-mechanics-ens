import math, random, pandas
 
def Vol1_s(dimension):
    return (math.pi ** (dimension / 2.0)) / math.gamma(dimension / 2.0 + 1.0)
    
def Vol1_s_est(dimensions, trials):
    n_hits = 0
    for i in range(trials):
        dists = [random.uniform(-1.0, 1.0) for _ in range(dimensions)]
        sum_dist = sum(d ** 2 for d in dists)
        if sum_dist < 1.0:
            n_hits += 1
    return n_hits / float(trials) * 2 ** dimensions, n_hits
    
dimensions = []
result     = []
trials     = 1000000

print '%i used for all' % trials
for d in range(1, 33):
    dimensions.append(str(d) + 'd')
    vol_est, n_hits = Vol1_s_est(d, trials)
    result.append({ 'estimation of Vol1_s(d)': vol_est,
                    'Vol1_s(d) (exact)':       Vol1_s(d),
                    'n_hits':                  n_hits })
    print d, n_hits, vol_est

ordered_cols = ['estimation of Vol1_s(d)', 'actual', 'n_hits']
print pandas.DataFrame(result, dimensions, columns=ordered_cols)
