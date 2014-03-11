import random, math

dimensions = 5
nsamples = 20
for sample in xrange(nsamples):
    R = [random.gauss(0.0, 1.0) for d in xrange(dimensions)]
    radius = math.sqrt(sum(x ** 2 for x in R))
    print [x / radius for x in R]

