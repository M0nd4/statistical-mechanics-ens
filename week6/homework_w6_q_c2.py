import math, random, pylab
 
def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))
 
def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x
 
beta = 20.0
N = 80
dtau = beta / N
n_steps = 100000
x = [0.0] * N
data = []
Weight_trott = lambda y: math.exp(sum(-a **2/ 2.0 * dtau for a in y))
cubic   = -1
quartic =  1
V = lambda x:  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4

for step in range(n_steps):
    Ncut = random.randint(0, N-1)
    # x_new = levy_free_path(x[0], x[0], dtau, N)
    x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    if random.uniform(0, 1) < min(1, Weight_trott(x_new) / Weight_trott(x)):
        x = x_new[:]
        k = random.randint(0, N - 1)
        data.append(x[k])
 
print len(data)
 
pylab.hist(data, bins=50, normed=True, label='QMC')
x_values = [0.1 * a for a in range (-30, 30)]
y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
                math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]
pylab.plot(x_values, y_values, label='exact')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 0.8])
pylab.legend()
ProgType = 'Levy_free_path'
pylab.title(ProgType + ' beta = ' + str(beta) + ', dtau = ' + str(dtau) +
            ', Nsteps = '+ str(n_steps))
pylab.savefig(ProgType + str(beta) + '.png')
pylab.show()
