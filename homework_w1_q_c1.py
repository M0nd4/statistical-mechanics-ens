import random, math

def markov_pi_all_data(N, delta):
    x, y = 1.0, 1.0
    data_sum = 0.0
    data_sum_sq = 0.0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x ** 2 + y ** 2 < 1.0:
            data_sum += 4.0
            data_sum_sq += 4.0 ** 2
    return data_sum / float(N), data_sum_sq / float(N)

n_trials = 2 ** 14
delta = 0.1
n_parties = 100
inside_error_bar = 0
for iteration in range(n_parties):
    mean, mean_square = markov_pi_all_data(n_trials, delta)
    naive_error = math.sqrt(mean_square  - mean ** 2) / math.sqrt(n_trials)
    error =  abs(mean - math.pi)
    if error < naive_error: 
        inside_error_bar += 1
    print mean, error, naive_error
    
print inside_error_bar / float(n_parties),'fraction: error bar including pi'
