import math, random, pylab
 
def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))
 
def levy_harmonic_path(xstart, dtau, N):
    xend = xstart
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x
    
def std_deviation(x, beta):
    return math.exp(- x ** 2 * math.tanh(beta / 2.0))
 
beta = 10.0
N = 80
dtau = beta / N
n_steps = 100000
x = [2.0] * N
data = []
acc = 0
xstart = 0.0
for step in range(n_steps):
    x = levy_harmonic_path(xstart, dtau, N)
    k = random.randint(0, N - 1)
    sigma = std_deviation(x[k], beta)
    xstart = random.gauss(0.0, sigma)
    data.append(x[k])
 
pylab.hist(data, bins=50, normed=True, label='QMC')
x_values = [0.1 * a for a in range (-30, 30)]
y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
                math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]
pylab.plot(x_values, y_values, label='exact')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 0.6])
pylab.legend()
ProgType = 'Standard_deviation_of_Levy_harm_path'
pylab.title(ProgType + '\nbeta = ' + str(beta) + ', dtau = ' + str(dtau) +
            ', Nsteps = '+ str(n_steps))
pylab.savefig(ProgType + str(beta) + '.png')
pylab.show()
