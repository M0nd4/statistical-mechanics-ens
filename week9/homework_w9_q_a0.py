import numpy, pylab
 
V = lambda x: -4.0 * x ** 2   -0.5 * x ** 3 +  x ** 4
b = lambda x: -4.0 * x ** 2
c = lambda x: -0.5 * x ** 3
d = lambda x: x ** 4
 
xs = numpy.linspace(-2000, 2000, 1000)
bs = b(xs)
cs = c(xs)
ds = d(xs)
ys = V(xs)
 
# pylab.plot(xs, bs, label='$y = -4x^2$')
# pylab.plot(xs, cs, label='$y = -0.5x^3$')
# pylab.plot(xs, ds, label='$y = x^4$')
pylab.plot(xs, ys, label='$y = -4x^2 - 0.5x^3 + x^4$')
pylab.legend()
pylab.savefig('two_local_minima')
pylab.show()
