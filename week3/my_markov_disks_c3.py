import cmath, math, os, random, pylab
 
def dist(x, y):
    ''' Distance between coords a and b i.e. the hypotenuse taking in to
        account periodicity - wrapping back around when > 1.0 '''
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return d_x**2 + d_y**2
   
def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius = sigma,  fc = 'r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    # pylab.show()

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: 
        d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: 
        d_y -= 1.0
    return d_x, d_y


def Psi_6(L, sigma_sq):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 **2 * sigma_sq and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0: 
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N) 

def do_sampling(L, eta, N, delta, n_steps):
    sigma = math.sqrt(eta / (N * math.pi))
    for steps in range(n_steps):
        a = random.choice(L)
        b = [(a[0] + random.uniform(-delta, delta)) % 1.0,
             (a[1] + random.uniform(-delta, delta)) % 1.0]
        min_dist = math.sqrt(min(dist(b, c) for c in L if c != a))
        if min_dist > 2 * sigma:
            a[:] = b
    return L

N = 64
eta = 0.72     # density
K = int(math.sqrt(N) + 0.5)
delta = 0.1
n_steps = 10000
 
# version of disk_configuration with thermally "warm" setup (made by running B5)
filename = 'disk_configuration.start.c4.txt'
 
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'Starting from file', filename
else:
    L = []
    for y in range(K):
        for x in range(K):
            L.append([float(x) / K + 0.5 / K, float(y) / K + 0.5 / K])
    print 'Starting from scratch'

while eta > 0.0:
    L = do_sampling(L, eta, N, delta, n_steps)
    # sample Psi
    eta = eta - 0.01

 show_conf(L, sigma,
          'Disk positions. C3',
          'periodic_disks_%i_iterations_c3.png' % n_steps)
 
