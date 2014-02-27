import math, os, random, pylab
 
def dist(x, y):
    ''' Distance between coords a and b i.e. the hypotenuse taking in to
        account periodicity - wrapping back around when > 1.0 '''
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x**2 + d_y**2)
   
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
    pylab.show()
 
N = 64
eta = 0.42     # density
K = int(math.sqrt(N) + 0.5)
sigma = math.sqrt(eta / (N * math.pi))
delta = 0.1
n_steps = 10000
 
filename = 'disk_configuration.txt'
 
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
 
for steps in range(n_steps):
    a = random.choice(L)
    b = [(a[0] + random.uniform(-delta, delta)) % 1.0,
         (a[1] + random.uniform(-delta, delta)) % 1.0]
    min_dist = min(dist(b, c) for c in L if c != a)
    if min_dist > 2 * sigma:
        a[:] = b
 
show_conf(L, sigma,
          'Disk positions after %i iterations in periodic box. B3' % n_steps,
          'periodic_disks_%i_iterations_b4.png' % n_steps)
 
f = open(filename, 'w')
for a in L:
    f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
